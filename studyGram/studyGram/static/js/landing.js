function submitForm(){
    if(document.getElementsByClassName('searchFieldForm')[0].children[2].value == ""){
        document.getElementsByClassName('searchFieldForm')[0].children[2].placeholder = "Wpisz wyszukiwaną frazę"
    }else{
        document.getElementsByClassName('searchFieldForm')[0].submit();
    }
}