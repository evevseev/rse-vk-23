import psycopg2


def get_connection(host, port, db, user, password):
    return psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)


def get_blocked_ips_count(cursor) -> int:
    cursor.execute("SELECT COUNT(*) FROM ips")
    return cursor.fetchone()[0]


def get_blocked_domains_count(cursor) -> int:
    cursor.execute("SELECT COUNT(*) FROM domains")
    return cursor.fetchone()[0]


def get_cases_count(cursor) -> int:
    cursor.execute("SELECT COUNT(*) FROM cases")
    return cursor.fetchone()[0]


def get_case(cursor, case_id):
    cursor.execute("SELECT * FROM cases WHERE id = %s", (case_id,))
    return cursor.fetchone()


def find_ip(cursor, ip):
    cursor.execute("SELECT ip, c.organization, c.number, c.date FROM ips "
                   "JOIN cases c on c.id = ips.case_id "
                   "WHERE ip = %s", (ip,))
    return cursor.fetchall()


def find_domain(cursor, domain):
    cursor.execute("SELECT domain, c.organization, c.number, c.date FROM domains "
                   "JOIN cases c on c.id = domains.case_id "
                   "WHERE domain LIKE '%%' || %s || '%%'", (domain,))
    return cursor.fetchall()
