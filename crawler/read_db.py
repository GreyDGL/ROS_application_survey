import sqlite3

# The script serves as a easy way to read the database

if __name__ == "__main__":
    db = sqlite3.connect("issues.db")
    cursor = db.cursor()
    # quick print
    # cursor.execute("SELECT issue_id, is_PR, fix_issue_id, issue_title FROM issues")
    # for row in cursor:
    #     print(row)

    # count the number of unique PRs
    cursor.execute("SELECT COUNT(DISTINCT issue_id) FROM issues WHERE is_PR = 1")
    print("Number of unique PRs: ", cursor.fetchone()[0])

    db.close()