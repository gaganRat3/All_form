#!/usr/bin/env python3
"""
Quick DB inspector for biodata_storysubmission table.
Run: python scripts/check_story_db.py
"""
import sqlite3
import json
import sys

DB = 'db.sqlite3'

def main():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute("PRAGMA table_info('biodata_storysubmission')")
        cols = cur.fetchall()
        print('TABLE_SCHEMA:')
        if not cols:
            print('No table biodata_storysubmission found.')
            return
        for c in cols:
            print(c)

        cur.execute(
            "SELECT id, boy_name, girl_name, girl_birth_date, boy_city, girl_city, who_is_filling, mobile_number, relationship_status, function_date, message, image, submitted_at FROM biodata_storysubmission ORDER BY id DESC LIMIT 20"
        )
        rows = cur.fetchall()
        print('\nRECENT_ROWS_COUNT:', len(rows))
        if rows:
            print(json.dumps(rows, default=str, ensure_ascii=False, indent=2))
        else:
            print('No rows')
    except Exception as e:
        print('ERROR:', e, file=sys.stderr)
        sys.exit(1)
    finally:
        if conn:
            try:
                conn.close()
            except Exception:
                pass

if __name__ == '__main__':
    main()
