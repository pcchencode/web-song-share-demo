create database test;
use test;

-- CREATE TABLE test_table (
--   name VARCHAR(20),
--   color VARCHAR(10)
-- );

CREATE TABLE `guitar_song` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL COMMENT '歌曲名稱',
  `author` varchar(15) DEFAULT NULL,
  `desc` varchar(100) DEFAULT NULL COMMENT '詳細描述',
  `url` varchar(500) DEFAULT NULL COMMENT '參考連結',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8 COMMENT='吉他曲目分享表';

-- INSERT INTO test_table
--   (name, color)
-- VALUES
--   ('dev', 'blue'),
--   ('pro', 'yellow');

-- INSERT INTO guitar_song
--   (`name`, `desc`, `url`)
-- VALUES
--   ('dev', 'blue', 'url11'),
--   ('pro', 'yellow', 'www');