"""

The appy.py mimics the structure you might use when creating an app.

It is the same as given in the SQLModel tutorial: https://sqlmodel.tiangolo.com/tutorial/code-structure

"""

from activities.starter.db_wk8.paralympics.database import create_db_and_tables, engine
from activities.starter.db_wk8.paralympics.query_service import QueryService


def main():
    create_db_and_tables()

    # Instance of the class that has the queries defined
    queries = QueryService(engine)

    # # Read all hosts, then iterate and print the results
    # print("Read all hosts")
    # for host in queries.read_hosts():
    #     print(host)
    #     print(repr(host))
    #
    # # Create a new host
    # created_host = queries.create_host(place_name="Potters Barsss", country_name="Great Britain")
    # print("Created host", created_host)
    # #
    # # Read one host
    # read_host = queries.read_host(created_host.id)
    # print("Read host by id", read_host)

    # # Update the host's place name
    # created_host.place_name = "Potters Bar"
    # updated_host = queries.update_host(created_host)
    # print("Updated host", updated_host)

    # # Delete the host
    # queries.delete_host(created_host.id)
    #
    # # 1. List all Paralympics (games) with their year and type.
    # result = queries.query_games_year_type()
    # print("All Paralympics (games) with their year and type.")
    # for r in result:
    #     print(f"{r[0]} - {r[1]}")

    # 2. List all winter Paralympics (games) with host name(s) and year.
    result = queries.query_games_type_with_host(event_type="summer")
    print("All winter Paralympics (games) with host name and year.")
    for r in result:
        print(f"{r[0]} - {r[1]}")
    #
    # # 3. Find all disabilities recorded in the database.
    # # 4. Get all Paralympics (Games) that took place after the year 2000.
    # # 5. Find all teams from a specific region (e.g. Oceania).
    # # 6. List all hosts located in a specific country (e.g., 'Italy') and the year they held the Paralympics.
    # # 7. Show all Paralympics (games) along with their host city and host country.
    # # 8. List all disabilities associated with each Paralympics (games).
    # # 9. Find all teams that participated in a specific Paralympics (game) (e.g., Tokyo 2016).
    # # 10. Find all the Paralympics that have competitors who are 'Amputees'
    # # 11. **Update** all instances of the disability 'Les Autres' to 'Other'


if __name__ == "__main__":
    main()
