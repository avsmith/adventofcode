#!/usr/bin/env python

DATA = """\
2
1
-1
-2
0
-1
1
-1
-7
-6
1
-4
-1
-12
-7
-3
-12
-5
-6
-13
-7
-17
-13
-11
-3
-7
-3
-2
-6
-27
-20
-15
-23
-23
-33
0
-10
-35
-29
-6
-10
-5
-20
-38
-30
-38
-12
-23
1
-4
-48
-45
-1
-30
-38
-27
-23
-53
-36
0
-3
-45
-32
-39
-32
-46
-23
-40
-10
-54
-38
-37
-44
1
-56
-11
-74
-41
-73
-34
-31
-42
-49
-75
-8
-48
-49
-82
-21
-58
-40
-75
-66
-31
-34
-35
-52
-23
-56
-58
-60
-18
-34
-50
-27
-1
-3
-6
-70
-93
-36
-15
-1
-51
0
-110
-7
-7
-56
-14
-66
-93
-56
-100
-19
-54
-79
-81
-19
-112
-13
-24
-40
-90
-8
-10
-14
-27
-62
-45
-137
-53
-53
-89
-48
-86
-139
-91
-146
-109
-52
-6
-32
-6
-113
-78
-12
-4
-113
-42
-145
-23
-64
-97
-98
-77
-155
-133
-65
-64
-59
-164
-155
-27
-65
-57
-133
-140
-95
-104
-46
-16
-139
-55
-15
-26
-63
-141
-93
-146
-51
-104
-84
-82
-87
-149
-19
-77
-154
-118
-96
-117
-96
-140
-47
-188
-158
-141
-192
-63
-58
-191
-63
-52
-135
-142
-109
-42
-134
-4
-11
-135
-13
-24
-39
-4
-183
-158
-25
-136
-35
-49
-54
-78
-18
-92
-19
-142
-40
-237
-119
-147
-198
-132
-73
-238
-106
-82
-51
-72
-9
-44
-151
-164
-35
-74
-252
-219
-40
-154
-229
-169
-130
-238
-64
-171
-174
-161
-67
-205
-160
-112
-191
1
-60
-147
0
-43
-67
-190
-256
-66
-189
-76
-86
-91
-243
-10
-142
-163
-52
-112
-162
-169
-269
-98
-188
-282
-212
-286
-28
-33
-6
-114
-89
-237
-90
-95
-202
-266
-72
-215
-50
-52
-78
-286
-32
-235
-7
-56
-194
-6
-32
-73
-48
-77
-69
-43
-279
-236
-79
-286
-105
-295
-61
-320
-130
-99
-90
-238
-294
-120
-9
-302
-327
-165
-267
-228
-250
-153
-28
-126
-187
-138
-163
-140
-26
-217
-197
-180
-338
-39
-71
-6
-56
-151
-272
-276
-246
-189
-183
-38
-249
0
-185
-8
-193
-213
-296
-3
-340
-76
-97
-87
-1
-172
-235
-38
-274
-169
-70
-162
-320
-78
-222
-69
-222
-219
-213
-313
-179
-182
-253
-135
-206
-54
-167
-101
-397
-367
-54
-143
-147
-156
-293
-144
-47
-254
-169
-307
-223
-339
-398
-414
-23
-107
-235
-302
-321
-111
-167
-345
-55
-64
-315
-266
-191
-265
-248
-426
-47
-409
-212
-212
-401
-87
-389
-146
-97
-65
-286
-447
-168
-26
-371
-153
-297
-285
-164
-215
-336
-14
-416
-278
-233
-234
-392
-113
-80
-237
-342
-85
0
-145
-75
-101
-88
-292
-285
-344
-254
-47
-310
-227
-60
-320
-102
-364
-131
-338
-17
-239
-124
-266
-380
-421
-217
-311
-287
-233
-223
-242
-16
-326
-407
-482
-470
-247
-365
-75
-278
-44
-404
-195
-348
-81
-309
-181
-176
-97
-274
-204
-485
-458
-364
-22
-89
-448
-235
-53
-50
-510
-89
-114
-158
-199
-189
-204
-528
-278
-274
-149
-208
-485
-313
-325
-246
-173
-478
-164
-153
-76
-407
-447
-109
-334
-199
-50
-361
-449
-338
-409
-66
-282
-510
-288
-380
-562
-543
-534
-500
-288
-526
-439
-142
-284
-421
-30
-243
-185
-433
-326
-102
-540
-391
-197
-580
-305
-436
-559
2
-30
-204
-97
-204
-207
-79
-329
-157
-284
-581
-182
-458
-232
-111
-352
-601
0
-245
-292
-167
-549
-456
-277
-63
-104
-493
-585
-369
-121
-122
-180
-466
-509
-405
-53
-555
-454
-549
-486
-80
-463
-385
-538
-274
-75
-90
-500
-434
-167
-142
-587
-92
-182
-95
-205
-49
-574
-352
-638
-204
-25
-375
-456
-400
-572
-37
-151
-81
2
-19
-579
-106
-344
-339
-188
-517
-12
-403
-623
-619
-429
-53
-227
-11
-548
-426
-115
-481
-425
-9
-43
-209
-145
-168
-241
-331
-521
-77
-642
-397
-37
-98
-333
-281
-162
-361
-119
-696
-440
-663
-347
-295
-692
-32
-331
-623
-275
-646
-517
-16
-193
-537
-403
-75
-607
-74
-393
-333
-665
-448
-419
-119
-213
-635
-668
-178
-46
-175
-537
-160
-467
-271
-594
-240
-262
-666
-205
-48
-319
-738
-240
-697
-685
-711
-98
-134
-28
-731
-317
-319
-288
-236
-425
-401
-625
-638
-496
-23
-751
-643
-382
-717
-269
-275
-764
-672
-758
-605
-530
-244
-526
-357
-175
-667
-282
-551
-642
-83
-116
-751
-381
-447
-266
-297
-88
-575
-246
-189
-662
-450
-91
-471
-209
-609
-151
-630
-345
-625
-743
-377
-789
-56
-370
-250
-661
-792
-560
-585
-231
-673
-725
-194
-317
-455
-234
-282
-516
-784
-2
-652
-427
-31
-755
-527
-725
-47
-606
-210
-172
-773
-819
-636
-348
-376
-700
-727
-156
-574
-414
-34
-439
-413
-604
-648
-381
-529
-82
-736
-816
-595
-352
-417
-836
-691
-660
-464
-314
-748
-698
-49
-97
-721
-294
-441
-446
-415
-187
-212
-506
-550
-131
-231
-637
-334
-853
-383
-407
-219
-518
-743
-83
-773
-162
-570
-611
-574
-355
-56
-775
-663
-131
-357
-560
-335
-390
-667
-516
-897
-752
-786
-246
-893
-693
-692
-647
-422
-361
-148
-231
-775
-62
-404
-783
-387
-559
-703
-403
-776
-588
-633
-831
-779
-23
-216
-381
-287
-517
-402
-814
-756
-646
-535
-270
-282
-157
-367
-356
-925
-333
-375
-469
-931
-347
-455
-942
-815
-311
-690
-65
-691
-64
-361
-409
-886
-488
-303
-806
-73
-653
-356
-71
-523
-370
-685
-526
-528
-519
-179
-762
-652
-388
-568
-296
-601
-822
-656
-258
-304
-670
-731
-352
-82
0
-116
-294
-652
-702
-933
-12
-348
-15
-662
-311
-695
-357
-872
-847
-791
-129
-574
-281
-42
-626
-36
-60
-864
-871
-246
-943
-500
-253
-684
-545
-1011
-330
-666
-468
-780
-596
-872
-812
-924
-836
-379
-528
-464
-99
-675
-317
-58
-641
-590
-227
-296
-303
-798
-39
-824
-300
-469
-251
-182
-40
-115
-997
-572
-743
-13
-557
-542
-832
-884
-385
-224
-932
-757
-405
-690
-745
-1008
-657
-846
-565
-508
-792
-245
-298
-793
-278
"""

origvalues = [int(i) for i in DATA.splitlines()]
testvalues = [0, 3, 0, 1, -3]


def num_steps(val, weird=False):
    pos = 0
    steps = 0
    while pos >= 0 and pos < len(val):
        offset = val[pos]
        if weird and offset >= 3:
            val[pos] -= 1
        else:
            val[pos] += 1
        pos += offset
        steps += 1
    return steps


values = list(origvalues)
print("Answer Star #1: {}".format(num_steps(values)))
values = list(origvalues)
print("Answer Star #2: {}".format(num_steps(values, True)))
