import os
import psycopg2

def check_supabase():
    # Usar IPv6 directa si el nombre de host falla
    host = "2600:1f13:838:6e17:187d:e4b5:7e7a:e4af"
    db_url = f"postgresql://postgres:MjpxIruvcgM7QKRP@[{host}]:5432/postgres"
    print(f"Connecting to: {db_url.split('@')[1]}")
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        # Comprobar específicamente la tabla 'producto'
        print("\n--- Checking 'producto' table ---")
        cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'producto'")
        cols = cur.fetchall()
        if not cols:
            print("Table 'producto' NOT found!")
        else:
            for col in cols:
                print(f"  {col[0]} ({col[1]})")
                
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_supabase()
