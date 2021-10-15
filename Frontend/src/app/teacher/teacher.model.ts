export class Teacher
{
    teacherId: number;
    name: string;
    orgName: string;
    aboutMe: string;
    email: string;

    public constructor(data) {
        this.teacherId = data && data.teacherId || "";
        this.name = data && data.name || "";
        this.orgName = data && data.orgName || "";
        this.aboutMe = data && data.aboutMe || "";
        this.email = data && data.email || "";        
    }
}