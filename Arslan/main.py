from fastapi import FastAPI, Depends, HTTPException
from models import  userStudy
from database import db_dependency
from database import engine


app = FastAPI()

@app.get('/user_study/{user_id}')
def user_study(user_id : int , db : db_dependency):
        user_study_rows = db.query(userStudy).filter(userStudy.user_id == {user_id}).all()
        path_dict = {}
        count_path_dict = {}
        if user_study_rows:
            for row in user_study_rows:
                if row.paths in path_dict:
                    count_path_dict[row.paths] += 1
                    path_dict[row.paths] += round((row.status/count_path_dict[row.paths]), 2)
                else:
                    path_dict[row.paths] = row.status
                    count_path_dict[row.paths] = 1
            
            each_path_status = list(path_dict.values())
            avg_total_status = sum(each_path_status)/len(each_path_status)
            path_dict["OverAll"] = round(avg_total_status, 2)
            
            return {"user_study_status":path_dict}
        else:
            raise HTTPException(status_code=404, detail= "user not found")

    
    


