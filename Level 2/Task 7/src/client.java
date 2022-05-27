public class client {

    //declared variables
    String client_name;
    int client_telephoneNumber;
    String client_emailAddress;
    String client_physicalAddress;

    //class initialized with parameters which contain specific conditions
    public client(String client_name, int client_telephoneNumber, String client_emailAddress,String client_physicalAddress) {

        //constructors
        this.client_name = client_name;
        this.client_telephoneNumber = client_telephoneNumber;
        this.client_emailAddress = client_emailAddress;
        this.client_physicalAddress = client_physicalAddress;
    }

    //Getters and Setters
    public String getClient_name() {
        return client_name;
    }
    public void setClient_name(String client_name) {this.client_name = client_name;}


    public int getClient_telephoneNumber() {
        return client_telephoneNumber;
    }
    public void setClient_telephoneNumber(int client_telephoneNumber) {this.client_telephoneNumber = client_telephoneNumber;}


    public String getClient_emailAddress() {
        return client_emailAddress;
    }
    public void setClient_emailAddress(String client_emailAddress) {this.client_emailAddress = client_emailAddress;}


    public String getClient_physicalAddress() {
        return client_physicalAddress;
    }
    public void setClient_physicalAddress(String client_physicalAddress) {this.client_emailAddress = client_physicalAddress;}


    //toString which displays output of data captured
    public String toString() {

        String output = " ";
        output += "Client name                              : " + client_name;
        output += "\nClient Telephone Number                : " + client_telephoneNumber;
        output += "\nClient email Address                   : " + client_emailAddress;
        output += "\nClient Physical Address                : " + client_physicalAddress;

        return output;
    }
}

