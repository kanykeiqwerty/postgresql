# 1. Найдите 10 самых часто встречающихся слов.
# select plaintext, occurences from wordform limit 10;

# 2. Найдите все слова, которые начинаются с буквы ‘a’, регистр не должен иметь
# значения.a’, регистр не должен иметь значения. 
# select plaintext from wordform where plaintext ilike 'a%';

# 3. Найдите все произведения,
# которые относятся к жанру ‘a’, регистр не должен иметь значения.p’.
# select title from work where genretype='p';

# 4. Найдите среднее количество параграфов в произведения жанра ‘a’, регистр не
# должен иметь значения.t’.
# select avg(totalparagraphs) from work where genretype='t';

# 5. Выведите все произведения, в которых количество слов выше среднего.
# select avg(totalwords) from work;
# select title, totalwords from work where totalwords>20563;

# 6. Выведите имя героя, количество его реплик, и произведение, в котором
# этот герой встречается.
# select charname, sum(speechcount), title from character join character_work on character.charid=character_work.charid inner join work on work.workid=character_work.workid group by charname, title;

# 7. Выведите среднее количество реплик героев в произведении ‘a’,
# регистр не должен иметь значения.Romeo and Juliet’.
# SELECT AVG(c.speechcount) FROM character AS c JOIN work AS w ON w.title ILIKE 'Romeo and Juliet';

#  8. Выведите общее
# количество слов в каждой из секций в таблице paragraph. 
# select section, sum(wordcount) from paragraph group by section;

# 9. Выведите
# всех героев, которые имеют от 15 до 30 реплик.
#  select charname, sum(speechcount) from character group by charname having sum(speechcount) between 15 and 30;

# 10. Выведите все произведения, которые были написаны в 17 веке
# select title, year from work where year between 1600 and 1700;

# 11. Найдите все произведения, которые имею в полном названии
# слово ‘a’, регистр не должен иметь значения.the’ 
# select longtitle from work where longtitle ilike '%a %';

# 12. Выведите всеуникальные секции в paragraph.
# select distinct section from paragraph;

# 13. Для каждой главы выведите: id, описание и название произведения, к которой
# относится данная глава.
# select chapter, chapterid,description, title from chapter join work on work.workid=chapter.workid group by chapter, chapterid, title; 

# 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя
# select paragraphnum, charname, sum(speechcount) from paragraph join character on character.charid=paragraph.charid group by paragraphnum, charname;

# 15. Для каждого параграфа выведите: номер параграфа, название произведения и
# год выхода этого произведения.
# select paragraphnum, title, year from paragraph join work on work.workid=paragraph.workid;




 




