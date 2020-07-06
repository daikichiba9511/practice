/*
sqlzoo : https://sqlzoo.net
参考　: https://github.com/jisaw/sqlzoo-solutions　
*/

/* 1. worldのテーブルから name, contnentを表示する　*/
SELECT name, continent, population FROM world;

/*2. world のテーブルからpopulationが200000000以上の国名を表示*/
SELECT name FROM world
WHERE population >= 200000000;

/* 3.  world のテーブルからpopulationが200000000以上の国名とひとり辺のgdpの表示*/
select
    name, gdp/population
from
    world
where
    population >= 200000000;

/* 4. world のテーブルからSouth America のnameとpopulationを1000000で割った数の表示*/
select
    name, population/1000000
from
    world
where
    continent = 'South America' ;

/* 5. worldのテーブルからフランス、ドイツ、イタリアの国名と人口の表示*/
select
    name, population
from
    world
where
    name in ('France', 'Germany', 'Italy') ;

/* 6. worldのテーブルからnameにUnitedを含むnameを表示*/
select
    name
from
    world
where
    name like '%United%' ;

/* 7. worldのテーブルからpopulation >= 250000000、またはarea >= 3000000のname, population, areaの表示*/
select
    name, population, area
from
    world
where
    population >= 250000000
    or area >= 3000000 ;

/*
8. 排他的論理和(XOR)の問題、定義が書いてなくて戸惑って答え探した。postgreSQLは排他的論理和がないらしい。
*/
select
    name, population, area
from
    world
where
    ( area > 3000000 and population <= 250000000)
    or (area <= 3000000 and population > 250000000);

/*
9. ROUND関数で小数点以下２桁に丸め込み
*/
select
    name, round(population/1000000, 2), round(gdp/1000000000, 2)
from
    world
where
    continent = 'South America'


/*
10. 
*/
select
    name, round(gdp/population/1000, 0)*1000
from
    world
where
    gdp >= 1000000000000;