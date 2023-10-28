from config import config
def main():
    params = config()
    conn = None
    user_interaction(params)
    database_interation()
    user_inter_with_class_DBManager(params)

if __name__ == '__main__':
    main()
