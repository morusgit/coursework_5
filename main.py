from project_utils.user_and_db_inter_functions import user_interaction, database_interaction, user_inter_with_class_DBManager

from config import config


def main():
    params = config()
    conn = None
    user_interaction(params)
    database_interaction()
    user_inter_with_class_DBManager(params)


if __name__ == '__main__':
    main()
