import psycopg2
import psycopg2.extras


class Postgres():
    def __init__(self):
        self.dbname = 'NBA '
        self.user = 'postgres'
        self.password = '1'
        self.host = 'localhost'
        self.connection_string = f"dbname='{self.dbname}' user='{self.user}' password='{self.password}' host='{self.host}'"
        self.conn = None
    def connect(self):
        try:
            self.conn = psycopg2.connect(self.connection_string)
            print("Database connection established")
        except Exception as e:
            print(f"Unable to connect to the database: {e}")
    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed")
    def query_choice(self,option):
        cur = self.conn.cursor()
        if option==1:
            team = input("Enter the Team Name: ")
            num = input("Enter the Team Number: ")
            statement = f"""
                INSERT INTO team
                VALUES ({num}, '{team}');
            """
            try:
                cur.execute(statement)
                self.conn.commit()
            except:
                print("Invalid Values. Please try again!")
                return
            print(f"Executed Command Successfully")
            return
        if option==2:
            playername = input("Enter the Name of the Player: ")
            statement = f"""
                DELETE FROM player
                WHERE "PLAYER_NAME" = '{playername}';
            """
            cur.execute(statement)
            self.conn.commit()
            print(f"Executed Command Successfully")
            return
        if option==3:
            table = 'player'
            where = input("Who do you want to Change? Enter ID:  ")
            set = input("Enter new Name: ")
            statement = f"""
                UPDATE {table}
                SET "PLAYER_NAME"= '{set}'
                WHERE "PLAYER_ID"={where};
            """
            cur.execute(statement)
            self.conn.commit()
            print(f"Executed Command Successfully")
            return
        if option==4:
            table = 'arena'
            condition = input("Enter the Team ID: ")
            statement = f"""
                SELECT *
                FROM {table}
                WHERE "TEAM_ID" = {condition};
            """
            cur.execute(statement)
            print(f"Executed Command Successfully")
            print(cur.fetchall())
            return
        if option==5:
            player = input("Enter the Name of the Player: ")
            statement = f"""
                SELECT Count(DISTINCT(team_id)) FROM seasons WHERE "player_id" in (Select "PLAYER_ID" FROM player WHERE "PLAYER_NAME" =  '{player}')
            """
            cur.execute(statement)
            print(f"Executed Command Successfully")
            print(cur.fetchall())
            return
        if option==6:
            player = input("Enter a Player Name: ")
            table = 'seasons'
            statement = f"""
                SELECT *
                FROM {table}
                WHERE "player_id" in (Select "PLAYER_ID" FROM player WHERE "PLAYER_NAME" =  '{player}')
                ORDER BY "season" ASC;
            """
            cur.execute(statement)
            print(f"Executed Command Successfully")
            print(cur.fetchall())
            return
        if option==7:
            table1 = 'city'
            table2 = 'arena'
            column = '"TEAM_ID"'
            statement = f"""
                SELECT *
                FROM {table1} JOIN {table2} 
                ON {table1}.{column} = {table2}.{column};
            """
            cur.execute(statement)
            print(f"Executed Command Successfully")
            print(cur.fetchall())
            return
        if option==8:
            statement = f"""
                SELECT COUNT(*),TEAM_ID FROM seasons GROUP BY "team_id";
            """
            cur.execute(statement)
            print(f"Executed Command Successfully")
            print(cur.fetchall())
            return
        if option==9:
            abbrev = input("Input the Abbreviation of the Team: ")
            statement = f"""
                SELECT COUNT(*)
                FROM seasons
                WHERE "team_id" IN (SELECT "TEAM_ID" FROM team WHERE "ABBREVIATION" = '{abbrev}');
            """
            cur.execute(statement)
            print(f"Executed Command Successfully")
            print(cur.fetchall())
            return
        if option==10:
            team = input("Enter the Team Name: ")
            num = input("Enter the Team Number: ")
            statement = f"""
                INSERT INTO team
                VALUES ({num}, '{team}');
            """
            try:
                cur.execute(statement)
                self.conn.commit()
                print(f"Executed Command Successfully")
            except:
                print("Error")
            return
        if option==11:
            team = input("Enter the Team Name: ")
            num = input("Enter the Team Number: ")
            statement = f"""
                INSERT INTO team
                VALUES ({num}, '{team}');
            """
            try:
                cur.execute(statement)
                self.conn.commit()
                print(f"Executed Command Successfully")
            except:
                print("Error")
            return
        
            



if __name__ == "__main__":
    
    db = Postgres()
    db.connect()
    current_choice = 1000
    print("""
    Welcome to the Database Management System 

    Choose an operation:
          
    1. Insert Data: 
    2. Delete Data: 
    3. Update Data: 
    4. Search Data: 
    5. Aggregate Functions: 
    6. Sorting: 
    7. Joins: 
    8. Grouping:
    9. Subqueries: 
    10. Transactions: 
    11. Error Handling: 
    12. Exit
    """)
    while True:
        choice = int(input("Enter your choice: "))
        if choice<=12:
            if choice == 12:
                confirm = input("Are you sure you want to exit? (yes/no): ")
                if confirm.lower() == "yes":
                    print("Exiting...")
                    break  
                else:
                    continue  
                
            db.query_choice(choice)
        else:
            print("Value is invalid, please enter a valid choice")
    print("Thanks for using this DBMS!")
    

