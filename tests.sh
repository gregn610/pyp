echo 'cat exercise_2.txt | ./pyp "s"'
cat exercise_2.txt | ./pyp -L "s"

echo 'cat exercise_2.txt | ./pyp "slash"'
cat exercise_2.txt | ./pyp -L "slash"

echo 'cat exercise_2.txt | ./pyp "slash[1]"'
cat exercise_2.txt | ./pyp -L "slash[1]"

echo 'cat exercise_2.txt | ./pyp "slash[-1]"'
cat exercise_2.txt | ./pyp -L "slash[-1]"

echo 'cat exercise_2.txt | ./pyp "slash[2:4]"'
cat exercise_2.txt | ./pyp -L "slash[2:4]"

echo 'cat exercise_2.txt | ./pyp "w[1]"'
cat exercise_2.txt | ./pyp -L "w[1]"

echo 'cat exercise_2.txt | ./pyp "w"'
cat exercise_2.txt | ./pyp -L "w"

echo 'cat exercise_2.txt | ./pyp "w[1]"'
cat exercise_2.txt | ./pyp -L "w[1]"

echo 'cat exercise_3.txt | ./pyp "s | s"'
cat exercise_3.txt | ./pyp -L "s | s"

echo 'cat exercise_3.txt | ./pyp "s"'
cat exercise_3.txt | ./pyp -L "s"
 
echo 'cat exercise_3.txt | ./pyp "slash | underscore"'
cat exercise_3.txt | ./pyp -L "slash | underscore"

echo 'cat exercise_3.txt | ./pyp "'_'.join(p.split('/'))"'
cat exercise_3.txt | ./pyp -L "'_'.join(p.split('/'))"

echo 'cat exercise_3.txt | ./pyp "'HELLO'.join(p.split('examples'))"'
cat exercise_3.txt | ./pyp -L "'HELLO'.join(p.split('examples'))"

echo 'cat exercise_3.txt | ./pyp "s[2:3] + s[1:5]"'
cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:5]"

echo 'cat exercise_3.txt | ./pyp "s[2:3] + s[1:1]"'
cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:1]"

echo 'cat exercise_3.txt | ./pyp "(s[2:3] + s[1:5])"'
cat exercise_3.txt | ./pyp -L "(s[2:3] + s[1:5])"

echo 'cat exercise_3.txt | ./pyp "s[2:3] + s[1:5]"'
cat exercise_3.txt | ./pyp -L "s[2:3] + s[1:5]"

echo 'cat exercise_3.txt | ./pyp "(s[2:3] + u[1:5])[1]"'
cat exercise_3.txt | ./pyp -L "(s[2:3] + u[1:5])[1]"

echo 'cat exercise_3.txt | ./pyp "(s[2:3] + u[1:5])[1]"'
cat exercise_3.txt | ./pyp -L "(s[2:3] + u[1:5])[1]"

echo 'cat exercise_3.txt | ./pyp "(s[2:3] + u[1:5])|p"'
cat exercise_3.txt | ./pyp -L "(s[2:3] + u[1:5])|p"

echo 'cat exercise_3.txt | ./pyp "(s[2:3] + u[1:5])|p[1]"'
cat exercise_3.txt | ./pyp -L "(s[2:3] + u[1:5])|p[1]"

echo 'cat exercise_3.txt | ./pyp "(s[2:3] + u[1:5])|u"'
cat exercise_3.txt | ./pyp -L "(s[2:3] + u[1:5])|u"

echo 'cat exercise_3.txt | ./pyp "p.replace('swin','tobyrosen')"'
cat exercise_3.txt | ./pyp -L "p.replace('swin','tobyrosen')"

echo 'cat exercise_3.txt | ./pyp "p.replace('tutorial_','')"'
cat exercise_3.txt | ./pyp -L "p.replace('tutorial_','')"

echo 'echo 'Hello' | ./pyp "'%s World'%p"'
echo 'Hello' | ./pyp -L "'%s World'%p"

echo 'echo 'Computer' | ./pyp "'Mr. %s, Do you want to see my %s '%(p,p)"'
echo 'Computer' | ./pyp -L "'Mr. %s, Do you want to see my %s '%(p,p)"

echo 'echo 'Computer' | ./pyp "'Mr. %s, Do you want to see my %s '%('Mac ' + p,p)"'
echo 'Computer' | ./pyp -L "'Mr. %s, Do you want to see my %s '%('Mac ' + p,p)"

echo 'echo 'Mac Computer' | ./pyp "'Mr. %s, Do you want to see my %s '%(p,p.replace('Mac ',''))"'
echo 'Mac Computer' | ./pyp -L "'Mr. %s, Do you want to see my %s '%(p,p.replace('Mac ',''))"

echo 'echo 'Computer' | ./pyp "'Mr. %s, Do you want to see my %s '%('Mac ' + p,p)"'
echo 'Computer' | ./pyp -L "'Mr. %s, Do you want to see my %s '%('Mac ' + p,p)"

echo 'echo 'Mac Computer' | ./pyp "'Mr. %s, Do you want to see my %s '%(p,p.replace('Mac ',''))"'
echo 'Mac Computer' | ./pyp -L "'Mr. %s, Do you want to see my %s '%(p,p.replace('Mac ',''))"

echo 'cat exercise_5.txt | ./pyp "p.kill('far')"'
cat exercise_5.txt | ./pyp -L "p.kill('far')"

echo 'echo 'I am all uppercase.' | ./pyp "p.upper()"'
echo 'I am all uppercase.' | ./pyp -L "p.upper()"

echo 'echo 'I am all LOWERcase.' | ./pyp "p.lower()"'
echo 'I am all LOWERcase.' | ./pyp -L "p.lower()"

echo 'echo '/MyDocuments/examples/pyp/source_file.psd' | ./pyp "p.file"'
echo '/MyDocuments/examples/pyp/source_file.psd' | ./pyp -L "p.file"

echo 'echo '/MyDocuments/examples/pyp/source_file.psd' | ./pyp "p.dir"'
echo '/MyDocuments/examples/pyp/source_file.psd' | ./pyp -L "p.dir"

echo 'cat exercise_7.txt | ./pyp "p.digits()"'
cat exercise_7.txt | ./pyp -L "p.digits()"

echo 'cat exercise_7.txt | ./pyp "p.isdigit()"'
cat exercise_7.txt | ./pyp -L "p.isdigit()"

echo 'cat exercise_7.txt | ./pyp "not p.isdigit()"'
cat exercise_7.txt | ./pyp -L "not p.isdigit()"

echo 'cat exercise_2.txt | ./pyp "keep('.mov')"'
cat exercise_2.txt | ./pyp -L "keep('.mov')"

echo 'cat exercise_2.txt | ./pyp "k('tiff','mymovie')"'
cat exercise_2.txt | ./pyp -L "k('tiff','mymovie')"

echo 'cat exercise_2.txt | ./pyp "l('mymovie')"'
cat exercise_2.txt | ./pyp -L "l('mymovie')"

echo 'cat exercise_2.txt | ./pyp "lose('tiff','mymovie')"'
cat exercise_2.txt | ./pyp -L "lose('tiff','mymovie')"

echo 'cat exercise_3.txt | ./pyp "p.trim()"'
cat exercise_3.txt | ./pyp -L "p.trim()"

echo 'cat exercise_3.txt | ./pyp "p.trim().trim()"'
cat exercise_3.txt | ./pyp -L "p.trim().trim()"

