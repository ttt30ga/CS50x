-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Run initial query at the crime scene
SELECT description
FROM crime_scene_reports
WHERE month = "7"
AND day = "28"
AND street = "Humphrey Street";

/*
Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time –
each of their interview transcripts mentions the bakery.
Littering took place at 16:36. No known witnesses.
*/

-- Check 3 witnesses interviews
SELECT name, transcript
FROM interviews
WHERE year = "2021"
AND month = "7"
AND day = "28";

/*
+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  name   |                                                                                                                                                     transcript                                                                                                                                                      |
+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Jose    | “Ah,” said he, “I forgot that I had not seen you for some weeks. It is a little souvenir from the King of Bohemia in return for my assistance in the case of the Irene Adler papers.”                                                                                                                               |
| Eugene  | “I suppose,” said Holmes, “that when Mr. Windibank came back from France he was very annoyed at your having gone to the ball.”                                                                                                                                                                                      |
| Barbara | “You had my note?” he asked with a deep harsh voice and a strongly marked German accent. “I told you that I would call.” He looked from one to the other of us, as if uncertain which to address.                                                                                                                   |
| Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
| Lily    | Our neighboring courthouse has a very annoying rooster that crows loudly at 6am every day. My sons Robert and Patrick took the rooster to a city far, far away, so it may never bother us again. My sons have successfully arrived in Paris.                                                                        |
| Emma    | I'm the bakery owner, and someone came in, suspiciously whispering into a phone for about half an hour. They never bought anything.                                                                                                                                                                                 |
+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Witnesses:
Ruth - Saw thief driving awar from bakery parking lot.
    CHECK BAKERY SECURITY LOGS: between 10:15 and 10:25
Eugene - Recognised thief. Saw withdrawing money from ATM on Leggett Street.
    CHECK ATM TRANSACTIONS: before 10:15
Raymond - Heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. Thief asked the person on the other end of the phone to purchase the flight ticket.
    CHECK PHONE CALL: around when thief was leaving the bakery. They called someone who talked to them for less than a minute. The thief then asked the person on the other end of the phone to purchase the flight ticket.
    CHECK FLIGHTS: origin, hour, minute, day, month
Emma - Noticed someone suspiciously whispering into a phone for about half an hour. They never bought anything.
*/

-- CHECK BAKERY SECURITY LOGS: between 10:15 and 10:25
-- Check license plates owners
SELECT bakery_security_logs.license_plate, people.name, people.phone_number, people.passport_number
FROM people
JOIN bakery_security_logs
ON people.license_plate = bakery_security_logs.license_plate
WHERE year = "2021"
AND month = "7"
AND day = "28"
AND hour = "10"
AND minute BETWEEN "15" AND "25";

/*
+---------------+---------+----------------+-----------------+
| license_plate |  name   |  phone_number  | passport_number |
+---------------+---------+----------------+-----------------+
| 5P2BI95       | Vanessa | (725) 555-4692 | 2963008352      |
| 94KL13X       | Bruce   | (367) 555-5533 | 5773159633      |
| 6P58WS2       | Barry   | (301) 555-4174 | 7526138472      |
| 4328GD8       | Luca    | (389) 555-5198 | 8496433585      |
| G412CB7       | Sofia   | (130) 555-0289 | 1695452385      |
| L93JTIZ       | Iman    | (829) 555-5269 | 7049073643      |
| 322W7JE       | Diana   | (770) 555-1861 | 3592750733      |
| 0NTHK55       | Kelsey  | (499) 555-9472 | 8294398571      |
+---------------+---------+----------------+-----------------+
*/

-- CHECK ATM TRANSACTIONS: before 10:15
SELECT atm_transactions.account_number, atm_transactions.transaction_type, atm_transactions.amount, atm_transactions.atm_location, people.name, people.phone_number, people.passport_number, person_id
FROM bank_accounts
JOIN people
ON bank_accounts.person_id = people.id
JOIN atm_transactions
ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_location = "Leggett Street"
AND transaction_type = "withdraw"
AND year = "2021"
AND month = "7"
AND day = "28";

/*
+----------------+------------------+--------+----------------+---------+----------------+-----------------+-----------+
| account_number | transaction_type | amount |  atm_location  |  name   |  phone_number  | passport_number | person_id |
+----------------+------------------+--------+----------------+---------+----------------+-----------------+-----------+
| 49610011       | withdraw         | 50     | Leggett Street | Bruce   | (367) 555-5533 | 5773159633      | 686048    |
| 26013199       | withdraw         | 35     | Leggett Street | Diana   | (770) 555-1861 | 3592750733      | 514354    |
| 16153065       | withdraw         | 80     | Leggett Street | Brooke  | (122) 555-4581 | 4408372428      | 458378    |
| 28296815       | withdraw         | 20     | Leggett Street | Kenny   | (826) 555-1652 | 9878712108      | 395717    |
| 25506511       | withdraw         | 20     | Leggett Street | Iman    | (829) 555-5269 | 7049073643      | 396669    |
| 28500762       | withdraw         | 48     | Leggett Street | Luca    | (389) 555-5198 | 8496433585      | 467400    |
| 76054385       | withdraw         | 60     | Leggett Street | Taylor  | (286) 555-6063 | 1988161715      | 449774    |
| 81061156       | withdraw         | 30     | Leggett Street | Benista | (338) 555-6650 | 9586786673      | 438727    |
+----------------+------------------+--------+----------------+---------+----------------+-----------------+-----------+
*/

-- Find match between Bakery security logs and ATM transactions
SELECT name, phone_number, passport_number, person_id
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = "2021"
    AND month = "7"
    AND day = "28"
    AND hour = "10"
    AND minute BETWEEN "15" AND "25"
    )
    AND account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE atm_location = "Leggett Street"
        AND transaction_type = "withdraw"
        AND year = "2021"
        AND month = "7"
        AND day = "28"
    );

/*
+-------+----------------+-----------------+-----------+
| name  |  phone_number  | passport_number | person_id |
+-------+----------------+-----------------+-----------+
| Bruce | (367) 555-5533 | 5773159633      | 686048    |
| Diana | (770) 555-1861 | 3592750733      | 514354    |
| Iman  | (829) 555-5269 | 7049073643      | 396669    |
| Luca  | (389) 555-5198 | 8496433585      | 467400    |
+-------+----------------+-----------------+-----------+
*/

-- CHECK PHONE CALLS:
-- Around when thief was leaving the bakery.
-- They called someone who talked to them for less than a minute.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket.
SELECT name, passport_number, person_id, phone_number
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = "2021"
    AND month = "7"
    AND day = "28"
    AND hour = "10"
    AND minute BETWEEN "15" AND "25"
    )
    AND account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE atm_location = "Leggett Street"
        AND transaction_type = "withdraw"
        AND year = "2021"
        AND month = "7"
        AND day = "28"
        )
        AND phone_number IN (
            SELECT caller
            FROM phone_calls
            WHERE duration <= "60"
            AND year = "2021"
            AND month = "7"
            AND day = "28"
        );
/*
+-------+----------------+-----------------+-----------+
| name  |  phone_number  | passport_number | person_id |
+-------+----------------+-----------------+-----------+
| Bruce | (367) 555-5533 | 5773159633      | 686048    |
| Diana | (770) 555-1861 | 3592750733      | 514354    |
+-------+----------------+-----------------+-----------+
*/

-- Check all calls from suspects (Bruce and Diana)
SELECT name, phone_number, phone_calls.id
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.caller
WHERE duration <= "60"
AND year = "2021"
AND month = "7"
AND day = "28";

/*
+---------+----------------+-----+
|  name   |  phone_number  | id  |
+---------+----------------+-----+
| Sofia   | (130) 555-0289 | 221 |
| Kelsey  | (499) 555-9472 | 224 |
| Bruce   | (367) 555-5533 | 233 | <-
| Kathryn | (609) 555-5876 | 234 |
| Kelsey  | (499) 555-9472 | 251 |
| Taylor  | (286) 555-6063 | 254 |
| Diana   | (770) 555-1861 | 255 | <-
| Carina  | (031) 555-6622 | 261 |
| Kenny   | (826) 555-1652 | 279 |
| Benista | (338) 555-6650 | 281 |
+---------+----------------+-----+
*/

-- Check phone calls ID
SELECT name, phone_number, phone_calls.id
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.receiver
WHERE duration <= "60"
AND year = "2021"
AND month = "7"
AND day = "28"
AND phone_calls.id = "233"
OR phone_calls.id = "255";

/*
+--------+----------------+-----+
|  name  |  phone_number  | id  |
+--------+----------------+-----+
| Robin  | (375) 555-8161 | 233 |
| Philip | (725) 555-3243 | 255 |
+--------+----------------+-----+
*/

-- CHECK FLIGHTS:
SELECT name, people.phone_number, people.passport_number, bank_accounts.person_id, passengers.seat, passengers.flight_id, flights.hour, flights.minute, flights.origin_airport_id, flights.destination_airport_id
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON flights.id = passengers.flight_id
WHERE license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = "2021"
    AND month = "7"
    AND day = "28"
    AND hour = "10"
    AND minute BETWEEN "15" AND "25"
    )
    AND account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE atm_location = "Leggett Street"
        AND transaction_type = "withdraw"
        AND year = "2021"
        AND month = "7"
        AND day = "28"
        )
        AND phone_number IN (
            SELECT caller
            FROM phone_calls
            WHERE duration <= "60"
            AND year = "2021"
            AND month = "7"
            AND day = "28"
        )
        AND flights.year = "2021"
        AND flights.month = "7"
        AND flights.day = "29"
        AND flights.hour BETWEEN "05" AND "12";

/*
+-------+----------------+-----------------+-----------+------+-----------+------+--------+-------------------+------------------------+
| name  |  phone_number  | passport_number | person_id | seat | flight_id | hour | minute | origin_airport_id | destination_airport_id |
+-------+----------------+-----------------+-----------+------+-----------+------+--------+-------------------+------------------------+
| Bruce | (367) 555-5533 | 5773159633      | 686048    | 4A   | 36        | 8    | 20     | 8                 | 4                      |
+-------+----------------+-----------------+-----------+------+-----------+------+--------+-------------------+------------------------+
*/

-- Check destination airport
SELECT city, full_name, abbreviation, id
FROM airports
WHERE id = "4";

/*
+---------------+-------------------+--------------+----+
|     city      |     full_name     | abbreviation | id |
+---------------+-------------------+--------------+----+
| New York City | LaGuardia Airport | LGA          | 4  |
+---------------+-------------------+--------------+----+
*/
