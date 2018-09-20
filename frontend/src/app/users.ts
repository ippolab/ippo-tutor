export class User {
    constructor (
        public username : string,
        public token : string,
        public istutor : boolean,
    ){}
}

export class Student {
    first_name: string;
    last_name: string;
    second_name: string;
    username: string;
    
    constructor(first_name: string, last_name: string, second_name: string, username: string){
        this.first_name = first_name;
        this.last_name = last_name;
        this.second_name = second_name;
        this.username = username;
    }
}