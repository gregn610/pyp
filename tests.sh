echo 'cat exercise_2.txt | ./pyp -L "s"'
cat exercise_2.txt | ./pyp -L "s"

echo 'cat exercise_2.txt | ./pyp -L "slash"'
cat exercise_2.txt | ./pyp -L "slash"

echo 'cat exercise_2.txt | ./pyp -L "slash[1]"'
cat exercise_2.txt | ./pyp -L "slash[1]"

echo 'cat exercise_2.txt | ./pyp -L "slash[-1]"'
cat exercise_2.txt | ./pyp -L "slash[-1]"

echo 'cat exercise_2.txt | ./pyp -L "slash[2:4]"'
cat exercise_2.txt | ./pyp -L "slash[2:4]"

echo 'cat exercise_2.txt | ./pyp -L "w[1]"'
cat exercise_2.txt | ./pyp -L "w[1]"

echo 'cat exercise_2.txt | ./pyp -L "w"'
cat exercise_2.txt | ./pyp -L "w"

echo 'cat exercise_2.txt | ./pyp -L "w[1]"'
cat exercise_2.txt | ./pyp -L "w[1]"

echo 'cat exercise_3.txt | ./pyp -L "s | s"'
cat exercise_3.txt | ./pyp -L "s | s"

echo 'cat exercise_3.txt | ./pyp -L "s"'
cat exercise_3.txt | ./pyp -L "s"
 
echo 'cat exercise_3.txt | ./pyp -L "slash | underscore"'
cat exercise_3.txt | ./pyp -L "slash | underscore"

echo 'cat exercise_3.txt | ./pyp -L "'_'.join(p.split('/'))"'
cat exercise_3.txt | ./pyp -L "'_'.join(p.split('/'))"

echo 'cat exercise_3.txt | ./pyp -L "'HELLO'.join(p.split('examples'))"'
cat exercise_3.txt | ./pyp -L "'HELLO'.join(p.split('examples'))"

echo 'cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:5]"'
cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:5]"

echo 'cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:1]"'
cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:1]"

echo 'cat exercise_3.txt | ./pyp -L "(s[2:3] + s[1:5])"'
cat exercise_3.txt | ./pyp -L "(s[2:3] + s[1:5])"

echo 'cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:5]"'
cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:5]"

