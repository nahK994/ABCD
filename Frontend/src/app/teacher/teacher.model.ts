export class Teacher
{
    teacherId: number;
    userName: string;
    email: string;

    public constructor(data) {
        this.teacherId = data && data.teacherId || "";
        this.userName = data && data.userName || "";
        this.email = data && data.email || "";
    }
}