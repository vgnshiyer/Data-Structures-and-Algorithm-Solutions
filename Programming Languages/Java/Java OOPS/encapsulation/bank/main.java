// package bank;

class Account {
    public String name;
    protected String email;
    private String password;
    
    Account() {
        System.out.println("Account opened!");
    }

    // getters and setters
    public String getPassword(){
        return this.password;
    }

    public void setPassword(String pass){
        this.password = pass;
    }
}

class main {
    public static void main(String args[]) {
        Account a = new Account();
        a.name = "sam";
        a.setPassword("shhhh");
        System.out.println(a.getPassword());
    }
}