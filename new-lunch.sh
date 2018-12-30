#!/bin/bash

set -eux

DATE=$1
REGEX="^[0-9]{4}-[0-9]{2}-[0-9]{2}$"


if [[ ! ( "${DATE}" =~ ${REGEX} ) ]]; then
    echo "Failed to regex match"
    exit 1
fi

YEAR=$(echo ${DATE} | cut -c 1-4)

FILE="_events/${YEAR}/${DATE}-lunch.md"

if [[ -e ${FILE} ]]; then
    echo "File: ${FILE} already exists!"
    exit 1
fi

START=$(date -d "${DATE} 12:00" +"%Y-%m-%d %H:%M:%S %z")
END=$(date -d "${DATE} 13:00" +"%Y-%m-%d %H:%M:%S %z")

cat - <<EOF > ${FILE}
---
dtend: ${END}
dtstart: ${START}
location: Formosa Cuisine
title: HV Open Lunch
type: lunch
---

Interested in talking more about Open Technology? Once a month we get
together for an informal lunch to talk tech, and catch up between
meetings. This is open to anyone.

Bring your ideas, open source questions, and grab some good food at
the same time!

EOF

echo "Wrote ${FILE}. Run ./meetup-sync.py ${FILE} to register it on meetup"
