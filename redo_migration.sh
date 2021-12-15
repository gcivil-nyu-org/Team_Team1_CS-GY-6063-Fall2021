# run the following command in terminal to redo migrations
# ./redo_migration.sh
echo "Removing migration files ..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
echo "Removing local database ..."
rm -vf db.sqlite3
echo "Redo migrations ..."
python manage.py makemigrations
python manage.py migrate
