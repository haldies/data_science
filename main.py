import psycopg2

conn_string = "postgresql://postgres.oozdmdvymgqafvyjgecq:sm2bTzvjUdJ7ut8T@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"


try:
    conn = psycopg2.connect(conn_string)
    print("Koneksi berhasil!")
    conn.close()
except Exception as e:
    print("Gagal konek:", e)
