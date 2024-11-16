from supabase import Client

def read(supabase: Client, table: str, query: str):
    return supabase.table(table).select(query).execute()

def write(supabase: Client, table: str, **kwargs):
    try:
        # Basic validation for kwargs
        if not kwargs:
            raise ValueError("Write Invalid | No data provided to insert.")

        # Attempt to insert the data into the specified table
        response = supabase.table(table).insert(kwargs).execute()

        # Check if there are any errors in the response
        if 'error' in response:
            raise Exception(f"Write Invalid | Database error: {response['error']}")

        return response

    except ValueError as ve:
        print(f"Write Invalid | ValueError: {ve}")
        return None

    except Exception as e:
        print(f"Write Invalid | An error occurred: {e}")
        return None