<?php
file_put_contents('record.txt', var_export($_POST['text'], true), FILE_APPEND);
