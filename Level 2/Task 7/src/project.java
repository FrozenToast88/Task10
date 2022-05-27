import java.time.LocalDate;

public class project {

    //declared variables
    int project_number;
    String project_name;
    String building_type;
    String project_address;
    int ERF_number;
    double project_feeTotal;
    double project_totalPaid_amount;
    LocalDate project_deadline;


    //class initialized with parameters which contain specific conditions
    public project (int project_number , String project_name , String building_type , String project_address , int ERF_number , double project_feeTotal
            , double project_totalPaid_amount , LocalDate project_deadline ) {

        //constructors
        this.project_number = project_number;
        this.project_name = project_name;
        this.building_type = building_type;
        this.project_address = project_address;
        this.ERF_number = ERF_number;
        this.project_feeTotal = project_feeTotal;
        this.project_totalPaid_amount = project_totalPaid_amount;
        this.project_deadline = project_deadline;

    }

    //Getters and Setters
    public int getProject_number() {
        return project_number;
    }
    public void setProject_number(int project_number) {this.project_number = project_number;}


    public String getProject_name() {
        return project_name;
    }
    public void setProject_name(String project_name) {this.project_name = project_name;}


    public String getBuilding_type() {
        return building_type;
    }
    public void setBuilding_type(String building_type) {this.building_type = building_type;}


    public String getProject_address() {
        return project_address;
    }
    public void setProject_address(String project_address) {this.project_address = project_address;}


    public int getERF_number() {
        return ERF_number;
    }
    public void setERF_number(int ERF_number) {this.ERF_number = ERF_number;}


    public double getProject_feeTotal() {
        return project_feeTotal;
    }
    public void setProject_feeTotal(double project_feeTotal) {this.project_feeTotal = project_feeTotal;}


    public double getProject_totalPaid_amount() {
        return project_totalPaid_amount;
    }
    public void setProject_totalPaid_amount(double project_totalPaid_amount) {this.project_totalPaid_amount = project_totalPaid_amount;}


    public LocalDate getProject_deadline() {
        return project_deadline;
    }
    public void setProject_deadline(LocalDate project_deadline) {this.project_deadline = project_deadline;}


    //toString which displays output of data captured
    public String toString() {

        String output = " ";
        output += "Project Number                  : " + project_number;
        output += "\n Project Name                 : " + project_name;
        output += "\n Building Type                : " + building_type;
        output += "\n Project Address              : " + project_address;
        output += "\n Project Fee Total            : " + project_feeTotal;
        output += "\n Project Total Paid Amount    : " + project_totalPaid_amount;
        output += "\n Project Deadline             : " + project_deadline;

        return output;
    }
}
