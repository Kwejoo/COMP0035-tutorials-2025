import time

from sqlmodel import Session, select

from activities.starter.db_wk8.comparison.models_n import Games, GamesHost, Host, create_norm_db
from activities.starter.db_wk8.comparison.models_u import Paralympics, create_db


def measure_query_time(session, stmt, iterations=100):
    """Measure average execution time for a given SQLModel query."""
    start = time.perf_counter()
    for _ in range(iterations):
        list(session.exec(stmt))  # Execute and fetch all results
    end = time.perf_counter()
    return (end - start) / iterations


def compare_query_time(engine1, stmt1, engine2, stmt2, iterations=100):
    """Compare execution time of two different queries on two different databases.

    parameters:
        engine1: SQLModel engine for the normalised database
        engine2: SQLModel engine for the unnormalised database
        stmt1: SQLModel query for the normalised database
        stmt2: SQLModel query for the unnormalised database
        iterations: int  Number of iterations to compare
    """
    with Session(engine1) as session1, Session(engine2) as session2:
        time1 = measure_query_time(session1, stmt1, iterations)
        time2 = measure_query_time(session2, stmt2, iterations)

    print("\n--- Comparison Results ---")
    print(f"DB 1 Query: {stmt1}\nAverage Time: {time1:.6f} seconds")
    print(f"DB 2 Query: {stmt2}\nAverage Time: {time2:.6f} seconds")

    if time1 < time2:
        print("✅ Normalised database query is faster.")
    elif time2 < time1:
        print("✅ Un-normalised database query is faster.")
    else:
        print("⚖️ Both queries have similar performance.")


def main():
    eng_n = create_norm_db()
    eng_u = create_db()

    statements_n = []
    statements_u = []

    # Queries
    # 1. List all Paralympics (games) with their year and type.
    stmt_n_1 = select(Games.year, Games.type)  # Normalised DB query
    statements_n.append(stmt_n_1)
    stmt_u_1 = select(Paralympics.year, Paralympics.type)  # Unnormalised DB query
    statements_u.append(stmt_u_1)

    # 2. List all winter Paralympics (Games) and include: host (place_name), year, number of participants.
    stmt_n_2 = (
        select(Host.place_name, Games.year, Games.participants)
        .join(GamesHost, GamesHost.games_id == Games.id)
        .join(Host, Host.id == GamesHost.host_id)
    )

    statements_n.append(stmt_n_2)
    stmt_u_2 = select(Paralympics.host, Paralympics.year, Paralympics.participants)
    statements_u.append(stmt_u_2)

    # 3. Find all disabilities recorded in the database.
    # 4. Get all Paralympics (Games) that took place after the year 2000.
    # 5. Find all teams from a specific country (e.g. Canada).
    # 6. List all hosts located in a specific country (e.g., 'Japan') and the year they held the Paralympics.
    # 7. Show all Paralympics (games) along with their host city and host country.
    # 8. List all disabilities associated with each Paralympics (games).
    # 9. Find all teams that participated in a specific Paralympics (game) (e.g., Tokyo 2016).
    # 10. Find all the Paralympics that have competitors who are 'Amputees'
    # 11. Update all instances of the disability 'Les Autres' to 'Other'

    for s in statements_n:
        with Session(eng_n) as session_n:
            result = session_n.exec(s)
            print(f"Result from normalised database for query {s}")
            for row in result:
                print(row)

    for s in statements_u:
        with Session(eng_u) as session_u:
            result = session_u.exec(s)
            print(f"Result from unnormalised database for query {s}")
            for row in result:
                print(row)


if __name__ == "__main__":
    main()
