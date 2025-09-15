import requests
import datetime
TOKEN="fvbjd35jnfdkbndfn@394nvf"
USERNAME="dheerajkrishnat29"

pixela_endpoint="https://pixe.la/v1/users"

parameter={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

resposne=requests.post(pixela_endpoint,json=parameter)

graph_endpoint="https://pixe.la/v1/users/dheerajkrishnat29/graphs"
graph_parameter={
    "id":"graph2",
    "name":"playing football",
    "unit":"hours",
    "type":"int",
    "color":"momiji"
}
Header={
    "X-USER-TOKEN":TOKEN
}
resposne_graph=requests.post(graph_endpoint,json=graph_parameter,headers=Header)

date=datetime.datetime(year=2025,month=6,day=25)
new_date=date.strftime("%Y%m%d")


parameter_for_post={
    "date":new_date,
    "quantity":"5"
}

parameter_for_put={
    "quantity":"10",
}

response_post=requests.post(f"{pixela_endpoint}/{USERNAME}/graphs/graph2",json=parameter_for_post,headers=Header)

update_post=requests.put(f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{new_date}",json=parameter_for_put,headers=Header)

delete_post=requests.delete(f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{new_date}",headers=Header)