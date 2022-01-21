using System;
using Models;
using System.Collections.Generic;

namespace DataStore
{
    public interface DataStoreInterface
    {
        Teacher getTeacher(Guid Id);
        List<Teacher> getTeachers();
        Guid createTeacher(Teacher Teacher);
        void updateTeacher(Teacher Teacher);
        void deleteTeacher(Teacher Teacher);
    }
}