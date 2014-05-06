echo 'cat exercise_2.txt | ./pyp "s"'
cat exercise_2.txt | ./pyp "s"

echo 'cat exercise_2.txt | ./pyp "slash"'
cat exercise_2.txt | ./pyp "slash"

echo 'cat exercise_2.txt | ./pyp "slash[1]"'
cat exercise_2.txt | ./pyp "slash[1]"

echo 'cat exercise_2.txt | ./pyp "slash[-1]"'
cat exercise_2.txt | ./pyp "slash[-1]"

echo 'cat exercise_2.txt | ./pyp "slash[2:4]"'
cat exercise_2.txt | ./pyp "slash[2:4]"

echo 'cat exercise_2.txt | ./pyp "w[1]"'
cat exercise_2.txt | ./pyp "w[1]"

echo 'cat exercise_2.txt | ./pyp "w"'
cat exercise_2.txt | ./pyp "w"

echo 'cat exercise_2.txt | ./pyp "w[1]"'
cat exercise_2.txt | ./pyp "w[1]"

echo 'cat exercise_3.txt | ./pyp "s | s"'
cat exercise_3.txt | ./pyp "s | s"

echo 'cat exercise_3.txt | ./pyp "s"'
cat exercise_3.txt | ./pyp "s"
 
echo 'cat exercise_3.txt | ./pyp "slash | underscore"'
cat exercise_3.txt | ./pyp "slash | underscore"

echo 'cat exercise_3.txt | ./pyp "'_'.join(p.split('/'))"'
cat exercise_3.txt | ./pyp "'_'.join(p.split('/'))"

echo 'cat exercise_3.txt | ./pyp "'HELLO'.join(p.split('examples'))"'
cat exercise_3.txt | ./pyp "'HELLO'.join(p.split('examples'))"

echo 'cat exercise_3.txt | ./pyp "s[2:3] + s[1:5]"'
cat exercise_3.txt | ./pyp "s[2:3] + s[1:5]"

echo 'cat exercise_3.txt | ./pyp "s[2:3] + s[1:1]"'
cat exercise_3.txt | ./pyp "s[2:3] + s[1:1]"

echo 'cat exercise_3.txt | ./pyp "(s[2:3] + s[1:5])"'
cat exercise_3.txt | ./pyp "(s[2:3] + s[1:5])"

echo 'cat exercise_3.txt | ./pyp "s[2:3] + s[1:5]"'
cat exercise_3.txt | ./pyp "s[2:3] + s[1:5]"

