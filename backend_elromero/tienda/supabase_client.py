import supabase

# Initialize the Supabase client
url = 'https://your-supabase-url.supabase.co'
key = 'your-supabase-key'
supabase_client = supabase.create_client(url, key)

# Function to fetch products

def fetch_products():
    response = supabase_client.table('products').select('*').execute()
    return response.data

# Function to fetch categories

def fetch_categories():
    response = supabase_client.table('categories').select('*').execute()
    return response.data
