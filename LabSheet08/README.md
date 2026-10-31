# Lab Sheet-08: Database Management using Python
MCA I Semester (Session 2026-2027)

All 30 programs use **SQLite** (built into Python, nothing to install) and one common
database file, `student_db.db`, which is created automatically in this folder.

## How to run
```
python p01_connect_database.py
python p03_create_students_table.py
...
```
Run any program on its own (each one creates the table/sample data it needs), or run them
in order 1 to 30. Keep `db_config.py` in the same folder, since all programs import it.

## Programs
| # | File | Task |
|---|------|------|
| 1 | p01_connect_database.py | Connect and show success message |
| 2 | p02_create_database.py | Create a new database |
| 3 | p03_create_students_table.py | Create `students` (id, name, age, marks) |
| 4 | p04_describe_table.py | Describe table structure |
| 5 | p05_list_tables.py | List all tables |
| 6 | p06_drop_table.py | Drop a table |
| 7 | p07_check_table_exists.py | Check if a table exists |
| 8 | p08_insert_single_record.py | Insert one record |
| 9 | p09_insert_multiple_records.py | Insert multiple records |
| 10 | p10_display_all_records.py | Display all records |
| 11 | p11_select_specific_columns.py | Display name and marks only |
| 12 | p12_marks_greater_than_80.py | Marks > 80 |
| 13 | p13_sort_by_marks_desc.py | Sort by marks, descending |
| 14 | p14_count_records.py | Count records |
| 15 | p15_top3_students.py | Top 3 scorers |
| 16 | p16_update_marks_by_id.py | Update marks by ID |
| 17 | p17_update_student_name.py | Update a student's name |
| 18 | p18_delete_by_id.py | Delete by ID |
| 19 | p19_delete_marks_below_40.py | Delete marks below 40 |
| 20 | p20_truncate_table.py | Truncate table, keep structure |
| 21 | p21_create_courses_table.py | Create and fill `courses` |
| 22 | p22_inner_join.py | INNER JOIN students and courses |
| 23 | p23_left_join.py | LEFT JOIN students and courses |
| 24 | p24_average_marks.py | Average marks |
| 25 | p25_group_by_age.py | Group by age with counts |
| 26 | p26_export_to_csv.py | Export to CSV |
| 27 | p27_import_from_csv.py | Import from CSV |
| 28 | p28_exception_handling.py | Show database errors via exception handling |
| 29 | p29_modular_insert_fetch.py | Functions to insert and fetch |
| 30 | p30_student_management_menu.py | Menu-driven Add/View/Update/Delete app |

## Notes
- Every program has comments, a `try-except-finally` block, parameterized queries (`?`),
  and closes the connection with `.close()`.
- To use MySQL instead: `pip install mysql-connector-python`, connect with
  `mysql.connector.connect(...)`, and replace `?` with `%s`. Equivalent MySQL commands
  (DESCRIBE, SHOW TABLES, TRUNCATE) are given in comments inside the relevant programs.
- Programs 16, 17, 18 use constants at the top (`STUDENT_ID`, `NEW_MARKS`, ...) that you can edit.
