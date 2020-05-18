import { Component, OnInit } from '@angular/core';
import { DbService } from '../services/db.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css']
})
export class LandingComponent implements OnInit {

  data:string=null;
  constructor(private router:Router,private db:DbService) {
    this.getData();
   }

  ngOnInit() {
  }

  goInsert(){
    this.router.navigate(['/insert']);
  }

  getData() {
    let docs=this.db.pull().subscribe(data =>{
      localStorage.setItem('jsonData', JSON.stringify(data));
      this.data=JSON.stringify(data);
    });
  }

  goLogin(){
    this.router.navigate(['/'])
  }

}
