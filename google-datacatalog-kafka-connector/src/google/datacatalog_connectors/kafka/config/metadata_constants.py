#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class MetadataConstants:
    CLUSTER_ID = "cluster_id"
    TOPICS = "topics"
    NUM_BROKERS = "num_brokers"
    NUM_PARTITIONS = "num_partitions"
    CLEANUP_POLICY = "cleanup_policy"
    TOPIC_NAME = "name"
    RETENTION_TIME = "retention_time"
    RETENTION_TIME_TEXT = "retention_time_as_text"
    RETENTION_SPACE = "retention_space"
    RETENTION_SPACE_TEXT = "retention_space_as_text"
    MIN_COMPACTION_LAG = "min_compaction_lag"
    MIN_COMPACTION_LAG_TEXT = "min_compaction_lag_text"
    MAX_COMPACTION_LAG = "max_compaction_lag"
    MAX_COMPACTION_LAG_TEXT = "max_compaction_lag_text"
    BOOTSTRAP_SERVER = "bootstrap_server"