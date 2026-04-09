from interactions import Role

gulag_role: Role = None

def setup_gulag_role(role: Role):
    global gulag_role
    if gulag_role is not None:
        print("gulag_role is already inited!")
        return
    gulag_role = role
    print("gulag_role is now inited!")

def check_gulag_role() -> bool:
    return gulag_role is not None

def get_gulag_role() -> Role:
    global gulag_role
    if gulag_role is None:
        print("gulag_role is not inited!")
        return None
    return gulag_role