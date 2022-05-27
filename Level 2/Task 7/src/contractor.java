public class contractor {

    //declared variables
    String contractor_name;
    int contractor_telephoneNumber;
    String contractor_emailAddress;
    String contractor_physicalAddress;

    //class initialized with parameters which contain specific conditions
    public contractor(String contract_name, int contract_telephoneNumber, String contractor_emailAddress,String contractor_physicalAddress) {

        //constructors
        this.contractor_physicalAddress = contractor_physicalAddress;
        this.contractor_name = contract_name;
        this.contractor_telephoneNumber = contract_telephoneNumber;
        this.contractor_emailAddress = contractor_emailAddress;
    }

    //Getters and Setters
    public String getContractor_name() {return contractor_name;}
    public void setContractor_name(String contractor_name) {this.contractor_name = contractor_name;}


    public int getContractor_telephoneNumber() {return contractor_telephoneNumber;}
    public void setContractor_telephoneNumber(int contractor_telephoneNumber) {this.contractor_telephoneNumber = contractor_telephoneNumber;}


    public String getContractor_emailAddress() {return contractor_emailAddress;}
    public void setContractor_emailAddress(String contractor_emailAddress) {this.contractor_emailAddress = contractor_emailAddress;}


    public String getContractor_physicalAddress() {return contractor_physicalAddress;}
    public void setContractor_physicalAddress(String contractor_physicalAddress) {this.contractor_physicalAddress = contractor_physicalAddress;}


    //toString which displays output of data captured
    public String toString() {

        String output = " ";
        output += "Contractor Name                          : " + contractor_name;
        output += "\nContractor Telephone Number           : " + contractor_telephoneNumber;
        output += "\nContractor Email Address              :  " +  contractor_emailAddress;
        output += "\nContractor Physical Address              :  " +  contractor_physicalAddress;

        return output;
    }
}




