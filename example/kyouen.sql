SELECT g.gamename as ゲーム名, g.median as 中央値, g.model as 機種, b.brandname as ブランド, g.sellday as 発売日
  FROM gamelist g
  INNER JOIN shokushu s
    ON s.game = g.id
  INNER JOIN brandlist b
    ON b.id = g.brandname
  WHERE s.shubetu = 5
  AND s.creater IN (3360, 5739, 5738)   -- 声優ID
  GROUP BY g.id, b.brandname
  HAVING COUNT(s) >= 3                  -- 入力した声優数に応じて変える
  ORDER BY g.id, g.gamename, g.sellday;