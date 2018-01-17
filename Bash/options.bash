#SWEN 503
#Mauricio Hernandez
#300412504
echo "WELCOME TO CONTACT LIST"

cfile="./contactlist.txt"

#ADD
function add (){
	if [ ! -e "$cfile" ]; then
 		 echo "haha"
		 chmod 777 "$cfile">>"$cfile"
	fi

	read -p "Name: " name
	read -p "Phone: " phone
	while ! [[ "$phone" =~ ^[0-9]+$ ]]; do
		echo "Only numbers please"
		read -p "Phone: " phone
	done
	read -p "Mail: " mail
	echo "$name $phone $mail" >> "$cfile"
	echo "Contact added successfully"
}

#REMOVE
function remove(){
	if [ ! -e "$cfile" ]; then
 		 echo "You don't have any contact"
	else
		read -p "Enter the name of contact to remove: " r_name
		sed -i.bak "/$r_name/d" "$cfile"
		echo "Contact removed successfully"
	fi
}

#SEARCH
function search_c(){
	if [ ! -e "$cfile" ]; then
 		 echo "You don't have any contact"
	else
		read -p "Enter the name to search: " search_name
		grep -i "$search_name" "$cfile"
	fi
}


#SHOW
function show(){
 if [ ! -e "$cfile" ]; then
 	echo "You don't have any contact"
 else
 	less "$cfile"
 fi
}

#UPDATE
function update(){
	echo "WARNING: If you have duplicate contact names they will be
	removed and replaced by a single contact with the updated information"
	if [ ! -e "$cfile" ]; then
 		echo "You don't have any contact"
	else
		read -p "Enter the name of contact to update: " u_name
		sed -i.bak "/$u_name/d" "$cfile"
		read -p "Phone: " phone
		while ! [[ "$phone" =~ ^[0-9]+$ ]]; do
			echo "Only numbers please"
			read -p "Phone: " phone
		done
		read -p "Mail: " mail
		echo "$u_name $phone $mail" >> "$cfile"
		echo "Contact updated succesfully"
	fi
}

#MENU
PS3="Please choose an option "
select option in add remove update search showAll quit
do
    case $option in
        add) 
						add;;
        remove) 
						remove;;
				update)
						update;;
				search)
						search_c;;
				showAll)
						show;;
        quit)
            break;;
     esac
done


