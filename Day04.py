input_str = """[1518-09-02 00:18] wakes up
[1518-03-08 00:37] falls asleep
[1518-04-03 00:19] falls asleep
[1518-09-12 00:02] falls asleep
[1518-03-05 00:59] wakes up
[1518-04-19 00:22] falls asleep
[1518-10-18 23:51] Guard #349 begins shift
[1518-09-14 23:59] Guard #1013 begins shift
[1518-06-13 00:32] wakes up
[1518-03-13 00:35] falls asleep
[1518-06-04 00:45] wakes up
[1518-04-13 00:01] falls asleep
[1518-11-08 00:58] wakes up
[1518-07-23 00:06] falls asleep
[1518-04-12 00:40] falls asleep
[1518-04-01 23:57] Guard #1013 begins shift
[1518-05-07 00:13] falls asleep
[1518-11-16 00:05] falls asleep
[1518-09-29 00:41] falls asleep
[1518-08-05 00:01] Guard #509 begins shift
[1518-04-13 00:22] falls asleep
[1518-10-27 00:01] Guard #1217 begins shift
[1518-03-02 23:57] Guard #1249 begins shift
[1518-06-03 00:36] wakes up
[1518-10-17 00:01] Guard #1733 begins shift
[1518-11-19 00:23] falls asleep
[1518-04-30 00:06] falls asleep
[1518-07-22 00:58] wakes up
[1518-08-31 00:00] Guard #211 begins shift
[1518-05-01 00:37] falls asleep
[1518-08-01 23:59] Guard #509 begins shift
[1518-07-14 00:49] falls asleep
[1518-11-19 00:34] wakes up
[1518-09-08 00:00] falls asleep
[1518-11-18 00:02] Guard #3541 begins shift
[1518-05-07 23:58] Guard #769 begins shift
[1518-04-11 00:43] wakes up
[1518-10-13 00:38] falls asleep
[1518-04-26 00:19] falls asleep
[1518-03-06 23:59] Guard #809 begins shift
[1518-11-01 00:53] wakes up
[1518-09-11 00:23] wakes up
[1518-11-01 00:26] falls asleep
[1518-10-07 00:12] falls asleep
[1518-05-03 00:24] falls asleep
[1518-11-23 00:49] wakes up
[1518-09-25 23:56] Guard #2663 begins shift
[1518-10-30 00:43] wakes up
[1518-02-27 00:38] falls asleep
[1518-08-23 00:02] Guard #769 begins shift
[1518-03-14 00:03] Guard #2039 begins shift
[1518-06-13 00:14] falls asleep
[1518-06-18 00:15] falls asleep
[1518-05-01 00:02] falls asleep
[1518-04-04 00:39] falls asleep
[1518-05-28 00:30] falls asleep
[1518-04-04 23:58] Guard #1321 begins shift
[1518-11-05 00:15] falls asleep
[1518-06-20 00:55] wakes up
[1518-10-21 00:52] wakes up
[1518-08-26 00:00] Guard #1987 begins shift
[1518-03-04 00:48] falls asleep
[1518-03-29 00:59] wakes up
[1518-06-05 00:00] falls asleep
[1518-10-15 00:25] wakes up
[1518-11-11 00:48] falls asleep
[1518-09-24 23:53] Guard #509 begins shift
[1518-04-04 00:35] wakes up
[1518-05-15 00:42] falls asleep
[1518-05-26 00:24] wakes up
[1518-06-05 00:44] wakes up
[1518-10-27 00:57] wakes up
[1518-03-15 00:38] falls asleep
[1518-03-08 00:56] falls asleep
[1518-09-19 00:00] Guard #1217 begins shift
[1518-10-28 00:36] falls asleep
[1518-11-07 23:56] Guard #877 begins shift
[1518-07-29 23:58] Guard #1867 begins shift
[1518-04-18 00:20] wakes up
[1518-09-19 23:56] Guard #191 begins shift
[1518-04-17 00:49] wakes up
[1518-04-16 00:00] Guard #1733 begins shift
[1518-11-03 00:46] falls asleep
[1518-10-20 00:33] falls asleep
[1518-10-21 00:00] Guard #349 begins shift
[1518-09-26 00:33] falls asleep
[1518-08-31 00:42] falls asleep
[1518-04-20 23:56] Guard #1733 begins shift
[1518-08-22 00:57] wakes up
[1518-07-14 23:58] Guard #1249 begins shift
[1518-04-11 00:37] falls asleep
[1518-10-02 00:30] wakes up
[1518-06-08 00:30] wakes up
[1518-10-23 00:28] wakes up
[1518-10-02 00:42] falls asleep
[1518-08-31 00:46] wakes up
[1518-10-06 00:59] wakes up
[1518-08-29 23:58] Guard #1217 begins shift
[1518-06-18 00:56] falls asleep
[1518-06-24 23:58] Guard #2347 begins shift
[1518-11-02 00:37] falls asleep
[1518-03-03 00:41] falls asleep
[1518-09-05 23:56] Guard #509 begins shift
[1518-10-31 00:41] falls asleep
[1518-06-25 00:51] wakes up
[1518-10-11 23:50] Guard #877 begins shift
[1518-03-24 00:21] falls asleep
[1518-08-20 00:48] wakes up
[1518-08-13 00:59] wakes up
[1518-10-15 00:56] falls asleep
[1518-04-27 00:27] wakes up
[1518-04-08 00:25] wakes up
[1518-06-05 00:13] falls asleep
[1518-08-06 00:29] falls asleep
[1518-08-17 00:52] wakes up
[1518-07-06 00:12] wakes up
[1518-08-19 00:57] wakes up
[1518-05-01 00:17] wakes up
[1518-06-27 00:16] falls asleep
[1518-04-17 00:47] falls asleep
[1518-11-23 00:56] falls asleep
[1518-05-24 00:43] falls asleep
[1518-05-12 00:42] falls asleep
[1518-09-03 00:31] wakes up
[1518-09-09 00:39] falls asleep
[1518-10-03 00:51] falls asleep
[1518-10-01 00:58] wakes up
[1518-10-29 00:19] wakes up
[1518-07-05 00:41] falls asleep
[1518-04-03 00:48] falls asleep
[1518-02-28 00:28] falls asleep
[1518-06-15 23:59] Guard #1013 begins shift
[1518-06-14 00:33] falls asleep
[1518-10-05 23:56] Guard #1987 begins shift
[1518-08-10 00:54] falls asleep
[1518-10-31 00:42] wakes up
[1518-06-26 00:17] wakes up
[1518-08-02 23:57] Guard #1217 begins shift
[1518-08-16 00:30] falls asleep
[1518-07-29 00:10] falls asleep
[1518-03-14 23:59] Guard #661 begins shift
[1518-05-20 00:41] falls asleep
[1518-09-25 00:06] wakes up
[1518-07-01 00:04] Guard #509 begins shift
[1518-05-03 00:25] wakes up
[1518-06-27 00:47] falls asleep
[1518-06-02 00:10] falls asleep
[1518-11-07 00:00] Guard #1013 begins shift
[1518-06-05 00:10] wakes up
[1518-08-09 00:04] Guard #661 begins shift
[1518-03-25 00:39] falls asleep
[1518-09-19 00:28] wakes up
[1518-08-26 00:52] wakes up
[1518-11-12 00:00] falls asleep
[1518-10-15 00:53] wakes up
[1518-06-12 00:31] wakes up
[1518-10-08 00:48] wakes up
[1518-09-27 00:49] falls asleep
[1518-03-10 00:56] wakes up
[1518-02-26 00:05] falls asleep
[1518-11-05 00:30] wakes up
[1518-04-01 00:04] falls asleep
[1518-05-11 00:46] wakes up
[1518-10-03 00:53] wakes up
[1518-07-18 00:51] falls asleep
[1518-02-27 00:04] Guard #1453 begins shift
[1518-09-24 00:03] Guard #1987 begins shift
[1518-05-31 00:09] falls asleep
[1518-07-30 00:42] falls asleep
[1518-05-31 00:33] wakes up
[1518-06-09 00:55] wakes up
[1518-07-06 23:51] Guard #2663 begins shift
[1518-09-01 23:52] Guard #1217 begins shift
[1518-09-10 00:57] wakes up
[1518-08-26 00:21] falls asleep
[1518-03-07 00:49] wakes up
[1518-04-08 00:36] falls asleep
[1518-10-25 00:01] falls asleep
[1518-08-25 00:37] wakes up
[1518-07-29 00:59] wakes up
[1518-04-03 00:20] wakes up
[1518-09-26 00:56] falls asleep
[1518-08-02 00:57] wakes up
[1518-09-26 00:49] wakes up
[1518-09-23 00:38] falls asleep
[1518-09-26 00:17] falls asleep
[1518-09-27 00:46] wakes up
[1518-03-05 00:14] falls asleep
[1518-04-03 23:50] Guard #877 begins shift
[1518-02-26 00:35] falls asleep
[1518-08-12 00:24] falls asleep
[1518-08-27 00:28] wakes up
[1518-09-29 00:49] wakes up
[1518-11-02 00:42] wakes up
[1518-03-29 00:17] falls asleep
[1518-09-23 00:30] wakes up
[1518-07-27 00:29] wakes up
[1518-09-20 00:26] falls asleep
[1518-07-18 00:09] falls asleep
[1518-05-29 23:52] Guard #2039 begins shift
[1518-05-08 00:53] wakes up
[1518-08-03 00:35] falls asleep
[1518-03-12 00:49] falls asleep
[1518-04-18 00:39] falls asleep
[1518-11-09 00:12] falls asleep
[1518-10-11 00:03] Guard #233 begins shift
[1518-11-07 00:36] falls asleep
[1518-09-07 00:52] wakes up
[1518-04-16 00:41] wakes up
[1518-03-01 00:58] wakes up
[1518-07-03 00:40] wakes up
[1518-05-18 00:56] wakes up
[1518-11-19 00:54] wakes up
[1518-10-30 00:38] falls asleep
[1518-06-04 00:30] wakes up
[1518-10-31 00:34] wakes up
[1518-08-07 00:59] wakes up
[1518-08-21 00:55] wakes up
[1518-08-05 00:11] falls asleep
[1518-03-15 00:49] wakes up
[1518-04-22 00:03] Guard #769 begins shift
[1518-10-28 00:58] wakes up
[1518-04-18 00:56] wakes up
[1518-11-13 00:10] wakes up
[1518-11-09 00:43] wakes up
[1518-07-06 00:03] falls asleep
[1518-10-31 00:31] falls asleep
[1518-08-01 00:02] Guard #1451 begins shift
[1518-05-26 00:38] falls asleep
[1518-08-10 00:47] falls asleep
[1518-07-11 00:55] wakes up
[1518-04-11 23:58] Guard #809 begins shift
[1518-05-08 23:58] Guard #1217 begins shift
[1518-09-27 23:59] Guard #3541 begins shift
[1518-10-17 00:39] wakes up
[1518-11-09 23:57] Guard #1733 begins shift
[1518-07-26 00:04] falls asleep
[1518-03-05 00:43] wakes up
[1518-10-25 00:48] wakes up
[1518-09-06 00:37] wakes up
[1518-04-17 00:31] wakes up
[1518-03-26 23:50] Guard #877 begins shift
[1518-09-05 00:41] wakes up
[1518-10-25 00:37] falls asleep
[1518-03-21 00:10] falls asleep
[1518-06-27 00:37] wakes up
[1518-06-03 00:09] falls asleep
[1518-11-18 00:21] falls asleep
[1518-11-02 00:48] wakes up
[1518-04-02 23:57] Guard #769 begins shift
[1518-04-22 23:56] Guard #1453 begins shift
[1518-10-09 23:56] Guard #769 begins shift
[1518-06-01 23:59] Guard #191 begins shift
[1518-06-27 00:50] wakes up
[1518-04-29 00:43] wakes up
[1518-11-02 23:58] Guard #1013 begins shift
[1518-09-01 00:01] Guard #2039 begins shift
[1518-02-25 00:27] falls asleep
[1518-07-20 00:09] falls asleep
[1518-08-07 00:31] falls asleep
[1518-06-13 00:51] wakes up
[1518-07-29 00:01] Guard #1733 begins shift
[1518-07-15 00:58] wakes up
[1518-07-11 00:04] Guard #809 begins shift
[1518-03-06 00:47] wakes up
[1518-05-07 00:30] wakes up
[1518-09-10 00:56] falls asleep
[1518-10-10 00:51] wakes up
[1518-03-21 00:53] wakes up
[1518-09-23 00:19] falls asleep
[1518-11-11 00:04] Guard #769 begins shift
[1518-10-04 00:04] Guard #2039 begins shift
[1518-09-01 00:47] falls asleep
[1518-10-05 00:27] falls asleep
[1518-03-13 00:37] wakes up
[1518-03-30 00:59] wakes up
[1518-06-15 00:31] falls asleep
[1518-06-04 00:38] falls asleep
[1518-11-05 00:49] wakes up
[1518-08-02 00:27] falls asleep
[1518-11-08 00:11] falls asleep
[1518-11-15 00:58] wakes up
[1518-04-01 00:52] wakes up
[1518-10-19 00:50] falls asleep
[1518-03-28 00:57] wakes up
[1518-09-10 00:19] falls asleep
[1518-11-04 00:58] wakes up
[1518-11-09 00:00] Guard #349 begins shift
[1518-06-23 00:27] falls asleep
[1518-09-20 00:42] wakes up
[1518-05-02 00:13] falls asleep
[1518-10-28 23:59] Guard #3541 begins shift
[1518-05-12 00:04] Guard #1013 begins shift
[1518-06-20 00:21] wakes up
[1518-04-30 00:00] Guard #1987 begins shift
[1518-03-26 00:18] falls asleep
[1518-09-21 00:57] wakes up
[1518-07-18 00:56] wakes up
[1518-06-11 23:51] Guard #1987 begins shift
[1518-08-28 00:10] falls asleep
[1518-06-11 00:30] wakes up
[1518-03-03 00:57] wakes up
[1518-06-28 23:49] Guard #3541 begins shift
[1518-04-10 00:45] wakes up
[1518-04-22 00:21] falls asleep
[1518-07-27 23:57] Guard #211 begins shift
[1518-05-13 23:56] Guard #1733 begins shift
[1518-11-08 00:44] falls asleep
[1518-09-06 00:57] wakes up
[1518-10-27 00:36] falls asleep
[1518-11-06 00:32] wakes up
[1518-07-24 23:57] Guard #661 begins shift
[1518-08-09 00:23] falls asleep
[1518-10-29 00:11] falls asleep
[1518-08-17 00:06] falls asleep
[1518-05-06 00:33] falls asleep
[1518-05-11 00:30] falls asleep
[1518-09-28 00:37] wakes up
[1518-04-24 00:27] wakes up
[1518-08-20 23:59] Guard #233 begins shift
[1518-08-23 00:38] falls asleep
[1518-09-17 00:51] wakes up
[1518-05-12 00:51] wakes up
[1518-05-25 00:51] falls asleep
[1518-08-06 00:03] Guard #877 begins shift
[1518-05-19 00:04] Guard #349 begins shift
[1518-09-29 00:02] Guard #1867 begins shift
[1518-07-19 00:51] wakes up
[1518-10-27 00:37] wakes up
[1518-08-10 00:49] wakes up
[1518-03-16 00:16] falls asleep
[1518-08-10 00:41] wakes up
[1518-10-26 00:31] wakes up
[1518-11-22 00:55] wakes up
[1518-05-19 00:41] wakes up
[1518-04-15 00:04] falls asleep
[1518-03-11 00:53] wakes up
[1518-09-02 23:56] Guard #1867 begins shift
[1518-10-12 00:42] wakes up
[1518-03-20 00:53] falls asleep
[1518-04-24 00:09] falls asleep
[1518-03-28 23:58] Guard #2039 begins shift
[1518-06-28 00:58] wakes up
[1518-07-25 23:52] Guard #509 begins shift
[1518-06-22 00:41] wakes up
[1518-06-11 00:34] falls asleep
[1518-10-03 00:48] wakes up
[1518-06-10 00:04] Guard #2039 begins shift
[1518-06-12 00:48] falls asleep
[1518-06-14 00:44] wakes up
[1518-06-12 00:59] wakes up
[1518-09-28 00:10] falls asleep
[1518-03-20 00:59] wakes up
[1518-11-20 23:56] Guard #1321 begins shift
[1518-04-30 00:43] wakes up
[1518-06-24 00:00] Guard #2663 begins shift
[1518-10-07 00:48] falls asleep
[1518-07-21 23:57] Guard #211 begins shift
[1518-11-04 00:56] falls asleep
[1518-05-13 00:59] wakes up
[1518-04-14 23:47] Guard #1249 begins shift
[1518-10-23 00:56] falls asleep
[1518-09-09 00:00] Guard #1867 begins shift
[1518-11-23 00:57] wakes up
[1518-03-06 00:13] falls asleep
[1518-03-31 00:56] wakes up
[1518-11-13 00:44] falls asleep
[1518-03-03 23:47] Guard #2039 begins shift
[1518-06-02 00:51] wakes up
[1518-05-13 00:42] falls asleep
[1518-08-28 23:57] Guard #1249 begins shift
[1518-06-30 00:22] falls asleep
[1518-08-13 00:28] falls asleep
[1518-03-17 00:47] wakes up
[1518-09-12 23:59] Guard #1453 begins shift
[1518-03-29 00:53] falls asleep
[1518-07-24 00:27] wakes up
[1518-09-15 00:34] falls asleep
[1518-05-14 00:47] wakes up
[1518-10-01 00:28] wakes up
[1518-09-11 00:44] falls asleep
[1518-07-27 00:00] Guard #2347 begins shift
[1518-08-12 00:03] Guard #661 begins shift
[1518-10-28 00:57] falls asleep
[1518-08-27 00:08] falls asleep
[1518-10-29 00:32] wakes up
[1518-05-25 00:52] wakes up
[1518-03-31 23:47] Guard #769 begins shift
[1518-04-07 00:59] wakes up
[1518-04-17 00:56] falls asleep
[1518-09-18 00:28] falls asleep
[1518-11-23 00:03] Guard #2663 begins shift
[1518-03-01 00:00] Guard #769 begins shift
[1518-04-14 00:43] wakes up
[1518-03-27 00:46] wakes up
[1518-09-24 00:56] wakes up
[1518-09-02 00:59] wakes up
[1518-03-23 23:56] Guard #1733 begins shift
[1518-11-16 00:55] wakes up
[1518-03-08 00:59] wakes up
[1518-09-25 00:38] wakes up
[1518-09-18 00:01] Guard #1249 begins shift
[1518-08-15 00:44] wakes up
[1518-07-03 00:00] Guard #1733 begins shift
[1518-09-04 00:49] wakes up
[1518-06-10 00:47] wakes up
[1518-03-16 00:52] wakes up
[1518-08-12 00:48] wakes up
[1518-03-12 00:00] Guard #1249 begins shift
[1518-09-16 00:23] falls asleep
[1518-09-14 00:57] wakes up
[1518-10-31 00:01] Guard #809 begins shift
[1518-04-25 00:51] wakes up
[1518-10-28 00:41] wakes up
[1518-07-09 23:56] Guard #809 begins shift
[1518-03-12 00:56] wakes up
[1518-03-23 00:53] falls asleep
[1518-10-31 00:47] falls asleep
[1518-04-22 00:57] wakes up
[1518-05-16 00:44] wakes up
[1518-04-22 00:54] falls asleep
[1518-08-12 00:18] wakes up
[1518-07-28 00:42] wakes up
[1518-03-18 00:29] falls asleep
[1518-11-15 00:30] falls asleep
[1518-10-30 00:52] falls asleep
[1518-11-16 23:50] Guard #509 begins shift
[1518-06-29 23:59] Guard #661 begins shift
[1518-10-31 00:55] wakes up
[1518-11-02 00:46] falls asleep
[1518-08-15 00:40] wakes up
[1518-08-06 00:37] wakes up
[1518-04-12 23:48] Guard #877 begins shift
[1518-10-16 00:02] Guard #809 begins shift
[1518-10-11 00:35] falls asleep
[1518-06-16 00:56] wakes up
[1518-07-30 00:11] wakes up
[1518-08-16 00:57] wakes up
[1518-10-12 23:56] Guard #1453 begins shift
[1518-03-22 00:05] falls asleep
[1518-07-25 00:59] wakes up
[1518-09-26 00:58] wakes up
[1518-04-26 23:56] Guard #233 begins shift
[1518-07-22 00:50] wakes up
[1518-07-14 00:37] wakes up
[1518-05-03 00:39] falls asleep
[1518-04-10 00:18] falls asleep
[1518-11-14 23:57] Guard #349 begins shift
[1518-02-28 00:20] falls asleep
[1518-06-11 00:55] wakes up
[1518-11-23 00:28] falls asleep
[1518-10-25 23:53] Guard #1867 begins shift
[1518-07-20 00:10] wakes up
[1518-10-21 00:27] falls asleep
[1518-07-11 00:43] falls asleep
[1518-06-24 00:11] falls asleep
[1518-11-03 00:48] wakes up
[1518-10-07 00:50] wakes up
[1518-06-06 00:58] wakes up
[1518-10-24 00:36] falls asleep
[1518-07-30 00:53] wakes up
[1518-05-10 00:03] Guard #1321 begins shift
[1518-08-14 00:25] falls asleep
[1518-03-13 00:02] Guard #3541 begins shift
[1518-03-13 00:26] wakes up
[1518-04-18 00:14] falls asleep
[1518-04-29 00:01] Guard #1733 begins shift
[1518-06-18 23:57] Guard #1733 begins shift
[1518-05-24 00:52] wakes up
[1518-03-30 00:49] falls asleep
[1518-04-18 00:48] falls asleep
[1518-03-27 00:57] wakes up
[1518-06-19 00:55] falls asleep
[1518-05-21 23:59] Guard #1217 begins shift
[1518-06-27 00:00] Guard #1217 begins shift
[1518-06-05 00:38] falls asleep
[1518-06-20 00:37] falls asleep
[1518-11-05 00:36] falls asleep
[1518-06-04 00:01] Guard #1987 begins shift
[1518-08-29 00:55] wakes up
[1518-07-27 00:23] falls asleep
[1518-09-02 00:05] falls asleep
[1518-05-26 00:57] falls asleep
[1518-11-03 00:36] wakes up
[1518-10-24 23:48] Guard #809 begins shift
[1518-07-12 00:53] falls asleep
[1518-08-28 00:02] Guard #1453 begins shift
[1518-08-16 00:55] falls asleep
[1518-03-05 00:01] Guard #877 begins shift
[1518-07-21 00:03] Guard #2039 begins shift
[1518-11-13 00:49] wakes up
[1518-06-09 00:00] Guard #1249 begins shift
[1518-08-23 00:55] wakes up
[1518-05-22 00:54] wakes up
[1518-09-16 23:59] Guard #349 begins shift
[1518-03-03 00:55] falls asleep
[1518-07-25 00:49] falls asleep
[1518-08-03 00:39] wakes up
[1518-03-30 00:46] wakes up
[1518-05-15 00:39] wakes up
[1518-08-10 23:46] Guard #809 begins shift
[1518-06-19 00:35] falls asleep
[1518-04-03 00:58] wakes up
[1518-07-02 00:11] falls asleep
[1518-07-19 23:59] Guard #2347 begins shift
[1518-03-01 00:13] falls asleep
[1518-11-17 00:29] wakes up
[1518-03-31 00:46] falls asleep
[1518-11-20 00:01] falls asleep
[1518-05-03 00:47] wakes up
[1518-03-04 00:01] falls asleep
[1518-08-18 00:50] wakes up
[1518-08-06 00:56] wakes up
[1518-10-14 00:38] wakes up
[1518-04-14 00:03] Guard #349 begins shift
[1518-04-09 00:28] wakes up
[1518-08-03 00:07] falls asleep
[1518-07-30 23:59] Guard #2347 begins shift
[1518-10-23 23:58] Guard #661 begins shift
[1518-08-16 00:02] Guard #2347 begins shift
[1518-06-24 00:36] wakes up
[1518-10-10 00:17] falls asleep
[1518-04-27 00:44] wakes up
[1518-02-26 00:29] wakes up
[1518-09-29 00:58] wakes up
[1518-04-06 00:12] falls asleep
[1518-07-05 00:02] Guard #1013 begins shift
[1518-03-15 23:59] Guard #3541 begins shift
[1518-07-02 00:00] Guard #1867 begins shift
[1518-08-15 00:18] falls asleep
[1518-05-04 00:32] falls asleep
[1518-04-23 00:42] wakes up
[1518-06-14 00:30] wakes up
[1518-03-30 23:54] Guard #2039 begins shift
[1518-07-16 23:57] Guard #1321 begins shift
[1518-08-15 00:01] Guard #211 begins shift
[1518-11-06 00:51] falls asleep
[1518-08-03 00:46] falls asleep
[1518-06-15 00:00] Guard #1013 begins shift
[1518-03-27 00:50] falls asleep
[1518-05-14 00:40] falls asleep
[1518-05-11 00:54] falls asleep
[1518-10-13 23:59] Guard #877 begins shift
[1518-07-07 00:12] wakes up
[1518-03-21 00:56] falls asleep
[1518-07-26 00:58] wakes up
[1518-04-30 23:53] Guard #661 begins shift
[1518-07-16 00:03] Guard #769 begins shift
[1518-09-07 00:00] Guard #2347 begins shift
[1518-05-14 23:57] Guard #509 begins shift
[1518-11-09 00:50] falls asleep
[1518-10-09 00:34] falls asleep
[1518-03-25 00:58] wakes up
[1518-03-22 00:56] wakes up
[1518-04-02 00:37] falls asleep
[1518-11-19 00:43] falls asleep
[1518-10-16 00:46] falls asleep
[1518-08-25 00:43] falls asleep
[1518-09-07 23:48] Guard #809 begins shift
[1518-08-26 00:55] falls asleep
[1518-07-29 00:36] falls asleep
[1518-05-25 00:05] falls asleep
[1518-03-19 00:42] falls asleep
[1518-08-28 00:56] wakes up
[1518-05-01 23:57] Guard #211 begins shift
[1518-09-08 00:53] wakes up
[1518-10-18 00:00] Guard #2039 begins shift
[1518-10-10 00:48] falls asleep
[1518-11-18 23:56] Guard #211 begins shift
[1518-07-05 00:57] wakes up
[1518-08-30 00:19] falls asleep
[1518-07-31 00:27] falls asleep
[1518-04-12 00:09] falls asleep
[1518-08-22 00:40] falls asleep
[1518-04-15 00:53] falls asleep
[1518-10-06 00:42] falls asleep
[1518-06-09 00:53] falls asleep
[1518-09-05 00:10] falls asleep
[1518-05-06 00:04] Guard #211 begins shift
[1518-05-30 00:05] falls asleep
[1518-11-17 00:00] falls asleep
[1518-11-12 00:57] wakes up
[1518-05-12 23:59] Guard #2347 begins shift
[1518-10-02 00:02] Guard #1987 begins shift
[1518-05-25 23:47] Guard #2663 begins shift
[1518-11-19 23:53] Guard #1987 begins shift
[1518-04-12 00:47] wakes up
[1518-06-22 00:47] falls asleep
[1518-08-06 00:07] falls asleep
[1518-09-22 00:55] wakes up
[1518-11-05 00:04] Guard #1733 begins shift
[1518-09-30 00:28] falls asleep
[1518-03-24 00:35] wakes up
[1518-05-20 00:43] wakes up
[1518-07-18 00:00] Guard #2039 begins shift
[1518-03-01 23:50] Guard #1453 begins shift
[1518-04-20 00:00] Guard #211 begins shift
[1518-03-10 00:08] falls asleep
[1518-06-19 00:56] wakes up
[1518-05-11 00:59] wakes up
[1518-04-26 00:59] wakes up
[1518-08-25 00:19] falls asleep
[1518-02-28 00:25] wakes up
[1518-07-08 23:59] Guard #211 begins shift
[1518-09-13 00:42] wakes up
[1518-07-12 00:55] wakes up
[1518-08-13 00:54] falls asleep
[1518-09-15 00:14] falls asleep
[1518-03-17 00:50] falls asleep
[1518-03-17 00:51] wakes up
[1518-04-28 00:14] falls asleep
[1518-10-06 00:55] falls asleep
[1518-05-07 00:03] Guard #1987 begins shift
[1518-10-22 00:34] falls asleep
[1518-02-26 00:36] wakes up
[1518-03-30 00:02] Guard #2039 begins shift
[1518-04-21 00:20] falls asleep
[1518-06-04 00:08] falls asleep
[1518-05-09 00:41] wakes up
[1518-05-17 00:47] wakes up
[1518-09-21 00:11] falls asleep
[1518-10-10 00:35] wakes up
[1518-07-13 00:16] falls asleep
[1518-05-05 00:52] falls asleep
[1518-03-14 00:33] falls asleep
[1518-04-27 00:48] falls asleep
[1518-08-08 00:36] falls asleep
[1518-04-10 00:00] Guard #1733 begins shift
[1518-05-15 00:50] wakes up
[1518-07-30 00:06] falls asleep
[1518-09-07 00:13] falls asleep
[1518-04-13 00:50] wakes up
[1518-10-26 00:04] falls asleep
[1518-05-04 00:52] wakes up
[1518-03-31 00:35] wakes up
[1518-04-25 00:00] Guard #1013 begins shift
[1518-09-16 00:56] wakes up
[1518-09-27 00:01] Guard #661 begins shift
[1518-04-17 00:29] falls asleep
[1518-05-05 00:37] wakes up
[1518-04-11 00:58] wakes up
[1518-09-05 00:00] Guard #509 begins shift
[1518-08-04 00:57] wakes up
[1518-10-14 00:10] falls asleep
[1518-07-02 00:58] wakes up
[1518-05-03 00:58] wakes up
[1518-08-15 00:56] wakes up
[1518-10-05 00:45] wakes up
[1518-04-14 00:28] falls asleep
[1518-03-30 00:41] falls asleep
[1518-06-09 00:31] falls asleep
[1518-08-07 23:58] Guard #211 begins shift
[1518-09-13 00:25] falls asleep
[1518-11-13 00:00] falls asleep
[1518-10-17 00:42] falls asleep
[1518-05-08 00:41] falls asleep
[1518-05-28 00:38] wakes up
[1518-03-08 00:38] wakes up
[1518-09-02 00:35] falls asleep
[1518-10-22 00:49] wakes up
[1518-04-06 23:56] Guard #1217 begins shift
[1518-06-30 00:51] wakes up
[1518-09-11 00:22] falls asleep
[1518-04-02 00:52] wakes up
[1518-08-27 00:55] wakes up
[1518-05-06 00:48] wakes up
[1518-09-14 00:44] wakes up
[1518-05-11 00:36] wakes up
[1518-02-25 23:53] Guard #211 begins shift
[1518-06-06 00:51] falls asleep
[1518-06-12 00:04] falls asleep
[1518-09-14 00:52] falls asleep
[1518-08-22 00:26] wakes up
[1518-10-02 00:57] wakes up
[1518-11-01 23:59] Guard #1733 begins shift
[1518-05-16 00:04] Guard #1733 begins shift
[1518-03-19 00:00] Guard #769 begins shift
[1518-10-15 00:42] falls asleep
[1518-09-03 23:56] Guard #191 begins shift
[1518-09-10 23:56] Guard #211 begins shift
[1518-05-20 00:47] falls asleep
[1518-06-18 00:57] wakes up
[1518-04-23 00:23] wakes up
[1518-05-29 00:04] Guard #2347 begins shift
[1518-05-16 00:25] falls asleep
[1518-06-20 23:50] Guard #1987 begins shift
[1518-11-10 00:39] wakes up
[1518-06-06 00:45] wakes up
[1518-08-03 00:28] falls asleep
[1518-08-26 00:43] wakes up
[1518-08-19 00:04] Guard #2663 begins shift
[1518-08-22 00:14] falls asleep
[1518-11-22 00:46] falls asleep
[1518-07-18 23:58] Guard #809 begins shift
[1518-04-04 00:55] wakes up
[1518-07-21 00:16] falls asleep
[1518-09-03 00:13] falls asleep
[1518-09-04 00:28] falls asleep
[1518-06-13 23:56] Guard #1013 begins shift
[1518-06-02 23:59] Guard #1987 begins shift
[1518-11-03 23:57] Guard #1453 begins shift
[1518-06-06 00:37] falls asleep
[1518-02-25 00:58] wakes up
[1518-06-28 00:04] Guard #1249 begins shift
[1518-09-14 00:01] falls asleep
[1518-05-20 00:55] wakes up
[1518-05-19 23:56] Guard #191 begins shift
[1518-07-03 23:58] Guard #661 begins shift
[1518-09-11 23:47] Guard #1733 begins shift
[1518-05-05 00:13] falls asleep
[1518-06-26 00:04] Guard #1013 begins shift
[1518-04-24 00:37] wakes up
[1518-04-23 00:33] falls asleep
[1518-04-23 23:59] Guard #1217 begins shift
[1518-09-19 00:08] falls asleep
[1518-03-19 00:55] wakes up
[1518-04-21 00:50] wakes up
[1518-04-13 00:06] wakes up
[1518-11-02 00:59] wakes up
[1518-04-25 23:58] Guard #233 begins shift
[1518-06-07 00:24] falls asleep
[1518-08-10 00:00] Guard #1217 begins shift
[1518-07-04 00:54] wakes up
[1518-07-11 23:56] Guard #191 begins shift
[1518-11-13 23:56] Guard #349 begins shift
[1518-09-01 00:51] wakes up
[1518-07-14 00:00] Guard #349 begins shift
[1518-05-09 00:47] falls asleep
[1518-04-17 00:04] Guard #509 begins shift
[1518-08-03 00:30] wakes up
[1518-05-16 23:58] Guard #769 begins shift
[1518-11-12 23:50] Guard #349 begins shift
[1518-07-12 00:12] falls asleep
[1518-10-13 00:15] wakes up
[1518-06-07 23:56] Guard #877 begins shift
[1518-10-19 00:03] falls asleep
[1518-10-13 00:09] falls asleep
[1518-07-16 00:15] falls asleep
[1518-09-06 00:42] falls asleep
[1518-07-18 00:37] wakes up
[1518-10-11 00:58] wakes up
[1518-06-06 00:03] Guard #233 begins shift
[1518-11-06 00:55] wakes up
[1518-07-09 00:15] falls asleep
[1518-10-01 00:22] falls asleep
[1518-03-25 00:29] wakes up
[1518-10-29 23:58] Guard #1733 begins shift
[1518-03-19 23:57] Guard #1013 begins shift
[1518-11-08 00:26] wakes up
[1518-10-08 00:44] falls asleep
[1518-05-15 00:21] falls asleep
[1518-08-14 00:49] wakes up
[1518-07-31 00:57] wakes up
[1518-03-02 00:01] falls asleep
[1518-06-22 00:59] wakes up
[1518-10-18 00:20] falls asleep
[1518-05-03 00:50] falls asleep
[1518-09-30 23:56] Guard #1217 begins shift
[1518-07-13 00:55] wakes up
[1518-05-19 00:29] falls asleep
[1518-06-16 23:59] Guard #809 begins shift
[1518-06-12 00:49] wakes up
[1518-03-27 00:04] falls asleep
[1518-04-16 00:32] falls asleep
[1518-09-30 00:49] wakes up
[1518-04-18 00:43] wakes up
[1518-11-15 00:25] wakes up
[1518-05-10 23:56] Guard #1987 begins shift
[1518-04-22 00:47] wakes up
[1518-11-21 23:58] Guard #3541 begins shift
[1518-09-22 00:03] Guard #2039 begins shift
[1518-06-14 00:15] falls asleep
[1518-03-04 00:55] wakes up
[1518-07-27 00:51] wakes up
[1518-06-16 00:30] falls asleep
[1518-10-04 00:50] wakes up
[1518-08-19 00:53] falls asleep
[1518-09-13 23:48] Guard #2347 begins shift
[1518-03-12 00:34] falls asleep
[1518-05-07 00:57] wakes up
[1518-06-18 00:47] wakes up
[1518-05-14 00:14] wakes up
[1518-05-18 00:46] falls asleep
[1518-06-04 23:48] Guard #1733 begins shift
[1518-07-03 00:07] falls asleep
[1518-07-09 00:53] wakes up
[1518-08-06 00:46] falls asleep
[1518-09-29 00:54] falls asleep
[1518-10-25 00:10] wakes up
[1518-08-03 00:54] wakes up
[1518-06-15 00:56] wakes up
[1518-09-09 23:57] Guard #1249 begins shift
[1518-06-10 00:10] falls asleep
[1518-10-27 00:52] falls asleep
[1518-05-25 00:46] wakes up
[1518-04-27 00:39] falls asleep
[1518-04-29 00:08] falls asleep
[1518-05-26 00:01] falls asleep
[1518-03-01 00:50] wakes up
[1518-09-23 00:57] wakes up
[1518-10-19 00:47] wakes up
[1518-07-01 00:36] falls asleep
[1518-07-19 00:39] falls asleep
[1518-05-29 00:59] wakes up
[1518-06-21 23:56] Guard #2039 begins shift
[1518-09-15 00:29] wakes up
[1518-08-09 00:43] wakes up
[1518-10-23 00:45] falls asleep
[1518-05-18 00:00] Guard #2347 begins shift
[1518-03-20 23:56] Guard #349 begins shift
[1518-06-22 00:40] falls asleep
[1518-10-15 00:18] falls asleep
[1518-10-27 00:07] falls asleep
[1518-05-01 00:48] wakes up
[1518-06-11 00:18] falls asleep
[1518-08-06 00:19] wakes up
[1518-02-24 23:58] Guard #2347 begins shift
[1518-09-15 00:56] wakes up
[1518-09-16 00:02] Guard #809 begins shift
[1518-09-25 00:15] falls asleep
[1518-04-25 00:46] falls asleep
[1518-11-01 00:00] Guard #3541 begins shift
[1518-10-21 23:58] Guard #1733 begins shift
[1518-05-19 00:50] falls asleep
[1518-06-08 00:53] falls asleep
[1518-10-03 00:23] falls asleep
[1518-10-03 00:00] Guard #2347 begins shift
[1518-03-14 00:55] wakes up
[1518-05-23 00:27] falls asleep
[1518-08-18 00:11] falls asleep
[1518-11-18 00:48] wakes up
[1518-04-04 00:01] falls asleep
[1518-07-12 00:36] wakes up
[1518-03-21 23:48] Guard #661 begins shift
[1518-08-08 00:53] wakes up
[1518-11-09 00:55] wakes up
[1518-09-22 00:23] falls asleep
[1518-04-13 00:35] falls asleep
[1518-08-31 00:29] wakes up
[1518-10-20 00:00] Guard #191 begins shift
[1518-05-19 00:53] wakes up
[1518-11-18 00:09] falls asleep
[1518-03-02 00:39] wakes up
[1518-04-08 00:22] falls asleep
[1518-08-10 00:56] wakes up
[1518-11-06 00:01] Guard #2347 begins shift
[1518-05-24 00:02] Guard #1249 begins shift
[1518-05-23 00:00] Guard #1013 begins shift
[1518-03-23 00:02] Guard #2039 begins shift
[1518-05-26 23:47] Guard #211 begins shift
[1518-05-05 00:03] Guard #2347 begins shift
[1518-08-25 00:00] Guard #211 begins shift
[1518-07-16 00:18] wakes up
[1518-08-24 00:02] Guard #1733 begins shift
[1518-03-23 00:58] wakes up
[1518-11-15 23:52] Guard #1987 begins shift
[1518-10-12 00:57] wakes up
[1518-09-23 00:04] Guard #661 begins shift
[1518-11-06 00:13] falls asleep
[1518-09-25 00:43] falls asleep
[1518-10-17 00:34] falls asleep
[1518-06-21 00:03] falls asleep
[1518-08-12 00:06] falls asleep
[1518-04-06 00:50] wakes up
[1518-04-15 00:50] wakes up
[1518-10-15 00:01] Guard #2039 begins shift
[1518-05-05 00:56] wakes up
[1518-03-11 00:00] Guard #661 begins shift
[1518-10-23 00:02] Guard #1867 begins shift
[1518-09-25 00:48] wakes up
[1518-03-06 00:03] Guard #1217 begins shift
[1518-06-09 00:44] wakes up
[1518-04-10 23:56] Guard #2347 begins shift
[1518-10-05 00:00] Guard #2663 begins shift
[1518-10-19 00:58] wakes up
[1518-03-03 00:43] wakes up
[1518-05-31 00:03] Guard #349 begins shift
[1518-06-20 00:18] falls asleep
[1518-07-14 00:53] wakes up
[1518-03-28 00:02] Guard #1249 begins shift
[1518-03-29 00:36] wakes up
[1518-05-22 00:24] falls asleep
[1518-05-23 00:49] wakes up
[1518-03-09 00:01] Guard #2311 begins shift
[1518-07-20 00:48] falls asleep
[1518-02-28 00:44] wakes up
[1518-03-17 00:29] falls asleep
[1518-09-30 00:00] Guard #2347 begins shift
[1518-03-11 00:11] falls asleep
[1518-11-17 00:48] falls asleep
[1518-05-07 00:38] falls asleep
[1518-05-27 00:43] wakes up
[1518-06-13 00:46] falls asleep
[1518-05-26 00:58] wakes up
[1518-05-04 00:04] Guard #2039 begins shift
[1518-03-31 00:04] falls asleep
[1518-06-29 00:37] wakes up
[1518-06-21 00:44] wakes up
[1518-04-06 00:00] Guard #661 begins shift
[1518-04-09 00:04] falls asleep
[1518-11-11 00:57] wakes up
[1518-10-30 00:55] wakes up
[1518-08-13 00:44] wakes up
[1518-05-11 00:43] falls asleep
[1518-04-23 00:06] falls asleep
[1518-10-07 00:00] Guard #3541 begins shift
[1518-04-09 00:35] falls asleep
[1518-04-27 00:57] wakes up
[1518-10-23 00:13] falls asleep
[1518-11-14 00:33] wakes up
[1518-04-13 00:29] wakes up
[1518-10-04 00:39] falls asleep
[1518-03-04 00:36] wakes up
[1518-04-09 00:52] wakes up
[1518-06-08 00:27] falls asleep
[1518-10-08 23:56] Guard #191 begins shift
[1518-04-07 00:54] wakes up
[1518-10-29 00:30] falls asleep
[1518-05-12 00:17] falls asleep
[1518-05-01 00:23] falls asleep
[1518-09-24 00:23] falls asleep
[1518-04-11 00:47] falls asleep
[1518-11-14 00:15] falls asleep
[1518-07-27 00:33] falls asleep
[1518-10-09 00:41] wakes up
[1518-05-09 00:58] wakes up
[1518-04-20 00:37] falls asleep
[1518-08-03 00:12] wakes up
[1518-10-12 00:45] falls asleep
[1518-02-28 00:00] Guard #1987 begins shift
[1518-07-15 00:54] falls asleep
[1518-05-27 00:00] falls asleep
[1518-06-01 00:42] wakes up
[1518-08-03 23:57] Guard #1867 begins shift
[1518-09-12 00:23] wakes up
[1518-10-23 00:47] wakes up
[1518-05-31 23:56] Guard #349 begins shift
[1518-07-04 00:40] falls asleep
[1518-03-09 23:56] Guard #1217 begins shift
[1518-03-25 00:09] falls asleep
[1518-08-24 00:08] falls asleep
[1518-06-25 00:44] falls asleep
[1518-07-21 00:56] wakes up
[1518-07-23 00:04] Guard #509 begins shift
[1518-06-28 00:48] falls asleep
[1518-06-29 00:01] falls asleep
[1518-10-17 00:50] wakes up
[1518-06-05 00:34] wakes up
[1518-04-07 00:17] falls asleep
[1518-03-07 00:40] falls asleep
[1518-04-20 00:53] wakes up
[1518-05-02 23:59] Guard #509 begins shift
[1518-07-22 00:55] falls asleep
[1518-09-27 00:54] wakes up
[1518-02-27 00:41] wakes up
[1518-05-21 00:21] falls asleep
[1518-10-02 00:22] falls asleep
[1518-07-24 00:14] falls asleep
[1518-08-13 23:59] Guard #211 begins shift
[1518-06-08 00:55] wakes up
[1518-06-13 00:02] Guard #509 begins shift
[1518-08-21 00:48] falls asleep
[1518-04-24 00:30] falls asleep
[1518-05-21 00:00] Guard #191 begins shift
[1518-08-15 00:52] falls asleep
[1518-11-03 00:21] falls asleep
[1518-08-10 00:26] falls asleep
[1518-08-17 23:59] Guard #1453 begins shift
[1518-08-19 23:56] Guard #661 begins shift
[1518-07-10 00:47] falls asleep
[1518-03-26 00:50] wakes up
[1518-09-26 00:27] wakes up
[1518-09-27 00:28] falls asleep
[1518-10-12 00:02] falls asleep
[1518-04-07 23:56] Guard #1987 begins shift
[1518-06-07 00:32] wakes up
[1518-07-01 00:58] wakes up
[1518-08-26 00:46] falls asleep
[1518-08-31 00:07] falls asleep
[1518-10-23 00:57] wakes up
[1518-05-12 00:33] wakes up
[1518-07-22 00:37] falls asleep
[1518-06-10 23:57] Guard #211 begins shift
[1518-08-26 23:56] Guard #349 begins shift
[1518-03-18 00:50] wakes up
[1518-07-10 00:56] wakes up
[1518-08-25 00:48] wakes up
[1518-04-07 00:57] falls asleep
[1518-08-06 23:56] Guard #2347 begins shift
[1518-07-29 00:29] wakes up
[1518-08-11 00:02] falls asleep
[1518-11-02 00:56] falls asleep
[1518-04-08 23:47] Guard #233 begins shift
[1518-11-18 00:18] wakes up
[1518-11-15 00:13] falls asleep
[1518-06-26 00:14] falls asleep
[1518-03-25 23:56] Guard #1249 begins shift
[1518-08-26 00:57] wakes up
[1518-04-27 00:15] falls asleep
[1518-07-14 00:24] falls asleep
[1518-05-21 00:37] wakes up
[1518-06-19 23:59] Guard #877 begins shift
[1518-08-30 00:47] wakes up
[1518-08-20 00:28] falls asleep
[1518-04-15 00:55] wakes up
[1518-08-24 00:54] wakes up
[1518-08-17 00:00] Guard #877 begins shift
[1518-04-17 00:58] wakes up
[1518-06-19 00:40] wakes up
[1518-03-05 00:46] falls asleep
[1518-10-24 00:52] wakes up
[1518-10-08 00:04] Guard #1867 begins shift
[1518-04-28 00:01] Guard #2663 begins shift
[1518-06-17 00:50] wakes up
[1518-08-05 00:52] wakes up
[1518-09-09 00:59] wakes up
[1518-11-11 23:51] Guard #1867 begins shift
[1518-08-13 00:02] Guard #877 begins shift
[1518-08-15 00:43] falls asleep
[1518-10-16 00:47] wakes up
[1518-11-10 00:24] falls asleep
[1518-03-17 00:04] Guard #769 begins shift
[1518-06-07 00:00] Guard #349 begins shift
[1518-03-25 00:01] Guard #509 begins shift
[1518-07-23 00:43] wakes up
[1518-09-11 00:47] wakes up
[1518-04-18 23:57] Guard #661 begins shift
[1518-10-28 00:00] Guard #1733 begins shift
[1518-03-18 00:02] Guard #2039 begins shift
[1518-06-23 00:33] wakes up
[1518-05-02 00:53] wakes up
[1518-08-27 00:43] falls asleep
[1518-04-12 00:35] wakes up
[1518-11-17 00:49] wakes up
[1518-05-09 00:23] falls asleep
[1518-04-08 00:56] wakes up
[1518-06-17 23:56] Guard #211 begins shift
[1518-10-20 00:50] wakes up
[1518-08-21 23:56] Guard #1733 begins shift
[1518-08-29 00:35] falls asleep
[1518-04-18 00:01] Guard #509 begins shift
[1518-09-17 00:28] falls asleep
[1518-10-01 00:32] falls asleep
[1518-05-26 00:50] wakes up
[1518-07-23 23:57] Guard #661 begins shift
[1518-07-28 00:41] falls asleep
[1518-08-16 00:35] wakes up
[1518-06-01 00:35] falls asleep
[1518-11-07 00:44] wakes up
[1518-11-20 00:25] wakes up
[1518-08-04 00:42] falls asleep
[1518-09-21 00:02] Guard #809 begins shift
[1518-04-28 00:49] wakes up
[1518-10-15 00:57] wakes up
[1518-05-27 23:58] Guard #349 begins shift
[1518-04-19 00:38] wakes up
[1518-10-13 00:56] wakes up
[1518-08-11 00:47] wakes up
[1518-06-17 00:33] falls asleep
[1518-06-22 23:58] Guard #1867 begins shift
[1518-10-18 00:58] wakes up
[1518-05-14 00:11] falls asleep
[1518-05-30 00:52] wakes up
[1518-10-07 00:25] wakes up
[1518-05-29 00:52] falls asleep
[1518-03-28 00:38] falls asleep
[1518-03-21 00:59] wakes up
[1518-03-13 00:12] falls asleep
[1518-07-13 00:00] Guard #1249 begins shift
[1518-05-01 00:34] wakes up
[1518-09-18 00:57] wakes up
[1518-03-07 23:58] Guard #2039 begins shift
[1518-10-06 00:48] wakes up
[1518-09-06 00:10] falls asleep
[1518-07-07 23:58] Guard #1321 begins shift
[1518-07-07 00:02] falls asleep
[1518-05-17 00:40] falls asleep
[1518-10-27 00:30] wakes up
[1518-09-25 00:05] falls asleep
[1518-06-12 00:56] falls asleep
[1518-07-20 00:57] wakes up
[1518-03-12 00:37] wakes up
[1518-09-10 00:53] wakes up
[1518-05-24 23:51] Guard #349 begins shift
[1518-03-01 00:57] falls asleep
[1518-07-05 23:51] Guard #877 begins shift"""

## Day 4

import datetime
## Use datetime.datetime.strptime(date_string, format) method
## to parse your string into a datetime object.
## eg. for use: datetime.datetime.strptime("1518-11-01 23:58", "%Y-%m-%d %H:%M")
## Then, it will be possible to organize the datetime objects in a list
## by using comparison <, >, or == just as with integers.
## eg. datetime.datetime.strptime("1518-11-01 23:58", "%Y-%m-%d %H:%M")
## <
## datetime.datetime.strptime("1518-11-02 00:00", "%Y-%m-%d %H:%M")
## -> True
## Source: https://docs.python.org/3/library/datetime.html

def parse_line(line, time_pattern = "%Y-%m-%d %H:%M"):
    ## line: one line from the input string in the format:
    ## [YYYY-MM-DD HH:mm] Guard's action
    ## Postcondition: returns a tuple in the format:
    ## (datetime_object, guard_action)    
    i_open_bracket = line.index("[")
    i_close_bracket = line.index("]")
    date_str = line[i_open_bracket + 1 : i_close_bracket]
    guard_action = line[i_close_bracket + 1:]


    guard_action = guard_action.strip()
    date_obj = datetime.datetime.strptime(date_str, time_pattern)
    
    return (date_obj, guard_action)
## 5, 7, 2, 3, 6, 10, 9 #piv = 3
## 


def qsort_find_wall(arr, lo, hi, tuple_index):
    pivot_index = int((lo + hi) / 2)
    pivot = arr[pivot_index][tuple_index]
    i, j = lo - 1, hi + 1
    while True:
        i += 1
        j -= 1
        while arr[i][tuple_index] < pivot:
            i += 1
        while arr[j][tuple_index] > pivot:
            j -= 1
        
        if j <= i:
            return j
        #swap
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp

def quick_sort_tuple(arr, lo, hi, tuple_index = 0):
    if lo < hi:
        wall = qsort_find_wall(arr, lo, hi, tuple_index)
        quick_sort_tuple(arr, lo, wall)
        quick_sort_tuple(arr, wall + 1, hi)

def organize_by_date(input_str):
    ## input_str: the puzzle's input, each entry divided by "\n"
    ## Postcondition: returns a list of tuples organized 
    ## the datetime object portion of the tuple
    sorted_records = []
    records = input_str.split("\n")
    for line in records:
        record = parse_line(line)
        sorted_records.append(record)
    quick_sort_tuple(sorted_records, 0, len(sorted_records) - 1)
    return sorted_records

##Ultimately, you want to a dict of the following format:
## {
## guard_id: 
##          {"total_slept": int, "sleep_by_mins":
##                                              {min1: 20m, min2: 30m, etc.}
##          }
## }
## Then, you can loop and find the highest guard_id["total_slept"]
## after finding the guard_id, you can loop through guard_id["sleep_by_mins"]
## to find the highest min

def extract_guard_id(action):
    ## action: a string containing "Guard #XXXX begins shift"
    ## returns id of guard
    import re
    
    reg = re.compile(r"#\d+")
    match_obj = reg.search(action)
    if match_obj:
        s = match_obj.group()
        s = s.replace("#", "")
        guard_id = int(s)
        return guard_id
    else:
        print(match_obj.string + "does not contain '#\d+' pattern")
        return None

def create_new_guard(sleep_dict, guard_id):
    ## void function, creates a new guard and initializes all sleep minutes to 0
    sleep_dict[guard_id] = {"total_slept": 0, "sleep_by_mins": {}}
    for i in range(60):
        sleep_dict[guard_id]["sleep_by_mins"][i] = 0
    #print(sleep_dict)

def update_sleep_dict(sleep_dict, guard_id, sleep_start, sleep_end):
    sleep_session = sleep_end - sleep_start
    sleep_dict[guard_id]["total_slept"] += sleep_session
    for minute in range(sleep_start, sleep_end):
        sleep_dict[guard_id]["sleep_by_mins"][minute] += 1

def organize_guards_by_sleep(records, I_DATE = 0, I_ACTION = 1):
    ## records: a sorted list of tuple records
    ## I_DATE, I_ACTION: index of date/action inside each tuple record
    ## returns double nested dict of following format:
    ## {
    ## guard_id1: 
    ##          {"total_slept": int, "sleep_by_mins":
    ##                                              {min1: 20m, min2: 30m, etc.}
    ##          },
    ## guard_id2: ...
    ## }
    
    #1) for each record, find out if a guard is starting shift or not
    sleep_dict = {} # the dict to be returned
    guard_id = -1
    sleep_start = -1
    sleep_end = -1
    sleep_session = 0
    still_asleep = False
    for record in records:
        #2) if yes, set guard as new guard
        if "begins shift" in record[I_ACTION]:
            if still_asleep: # to cover the case in which the previous guard sleeps
                #past minute 59
                still_asleep = False
                sleep_end = 60
                update_sleep_dict(sleep_dict, guard_id, sleep_start, sleep_end)
            #2a) if guard_id doesn't exist in sleep_dict, create new
            #2b) set total_slept & minutes' values to 0
            guard_id = extract_guard_id(record[I_ACTION])
            if guard_id not in sleep_dict:
                create_new_guard(sleep_dict, guard_id)
            sleep_start = -1
            sleep_end = -1
            continue
        # what if guard falls asleep through minute 59? is there a "wakes up"?
        #3) if not, guard is the previous set guard
        #4) find fall asleep time (if any)
        if "falls asleep" in record[I_ACTION]:
            sleep_start = record[I_DATE].minute
            still_asleep = True
        #5) find wake up time (if any)
        elif "wakes up" in record[I_ACTION]:
            still_asleep = False
            sleep_end = record[I_DATE].minute
            #6) find total sleep time and add to {guard_id["total_slept"]}
            #7) loop through asleep time until awake time and add 1 to each min
            ## he was asleep            
            update_sleep_dict(sleep_dict, guard_id, sleep_start, sleep_end)
        else:
            print("You did not think of this action: " + record[I_ACTION])
    return sleep_dict

def find_sleepiest_minute(sleep_dict, guard_id):
    mins_dict = sleep_dict[guard_id]["sleep_by_mins"]
    sleepiest_minute = -1 # the key
    max_sleepiest_minute = 0 # the value
    for m, num_times_slept in mins_dict.items():
        #print(str(m) + " : " + str(num_times_slept))
        if num_times_slept > max_sleepiest_minute:
            sleepiest_minute = m
            max_sleepiest_minute = num_times_slept
    return (sleepiest_minute, max_sleepiest_minute)

def find_sleepy_guard(sleep_dict, part2 = True):
    ## returns (int, int) tuple representing (guard_id, most_slept_minute)
    most_slept_minutes = 0
    sleepiest_guard = -1
    if not part2:
        for guard_id, guard_sleep_dict in sleep_dict.items():
            if guard_sleep_dict["total_slept"] > most_slept_minutes:
                sleepiest_guard = guard_id
                most_slept_minutes = guard_sleep_dict["total_slept"]

        mins_dict = sleep_dict[sleepiest_guard]["sleep_by_mins"]
        #print(mins_dict)
        sleepiest_minute = -1
        max_sleepiest_minute = 0
        for m, num_times_slept in mins_dict.items():
            #print(str(m) + " : " + str(num_times_slept))
            if num_times_slept > max_sleepiest_minute:
                sleepiest_minute = m
                max_sleepiest_minute = num_times_slept
    else:
        sleepiest_minute = -1
        max_sleepiest_minute = 0
        for guard_id, guard_sleep_dict in sleep_dict.items():
            cur_min, cur_max = find_sleepiest_minute(sleep_dict, guard_id)
            if cur_max > max_sleepiest_minute:
                sleepiest_guard = guard_id
                sleepiest_minute = cur_min
                max_sleepiest_minute = cur_max
    return (sleepiest_guard, sleepiest_minute)

if __name__ == "__main__":
    records = organize_by_date(input_str)
    sleep_dict = organize_guards_by_sleep(records)
    sleepiest_guard, sleepiest_minute = find_sleepy_guard(sleep_dict)
    print("sleepiest guard: " + str(sleepiest_guard))
    print("sleepiest minute: " + str(sleepiest_minute))
    print("multiplied: " + str(sleepiest_guard * sleepiest_minute))
