from db.database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print('Error: ' + str(type(e)))
    finally:
        db.close()
