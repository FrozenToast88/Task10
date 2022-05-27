public class architect {

        //declared variables
        String architect_name;
        int architect_telephoneNumber;
        String architect_emailAddress;
        String architect_physicalAddress;

        //class initialized with parameters which contain specific conditions
        public architect (String architect_name , int architect_telephoneNumber , String architect_emailAddress , String architect_physicalAddress ) {

            //constructors
            this.architect_name = architect_name;
            this.architect_telephoneNumber = architect_telephoneNumber;
            this.architect_emailAddress = architect_emailAddress;
            this.architect_physicalAddress = architect_physicalAddress;

        }

        //Getters and Setters
        public String getArchitect_name(){return architect_name;}
        public void setArchitect_name(String architect_name){this.architect_name = architect_name;}


        public int getArchitect_telephoneNumber(){
            return architect_telephoneNumber;
        }
        public void setArchitect_telephoneNumber(int architect_telephoneNumber) {this.architect_telephoneNumber = architect_telephoneNumber;}


        public String getArchitect_emailAddress(){
            return architect_emailAddress;
        }
        public void setArchitect_emailAddress(String architect_emailAddress){this.architect_emailAddress = architect_emailAddress;}


        public String getArchitect_physicalAddress(){
            return architect_physicalAddress;
        }
        public void setArchitect_physicalAddress(String architect_physicalAddress){this.architect_physicalAddress = architect_physicalAddress;}



    //toString which displays output of data captured
    public String toString() {

        String output = " ";
        output += " Architect Name:                             : " + architect_name;
        output += "\n Architect Telephone Number:               : " + architect_telephoneNumber;
        output += "\n Architect Email Address:                  : " + architect_emailAddress;
        output += "\n Architect Physical Address:                  : " + architect_physicalAddress;

        return output;
    }
}
