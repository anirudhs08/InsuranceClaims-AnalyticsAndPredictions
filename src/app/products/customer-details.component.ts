import { Component, OnInit } from '@angular/core';
import * as myFile from './myFile.txt';
import { ProductService } from './product.service';
import { ICustomer } from './customer';

@Component({
  selector: 'pm-customer-details',
  templateUrl: './customer-details.component.html',
  styleUrls: ['./customer-details.component.css']
})
export class CustomerDetailsComponent implements OnInit {
  pageTitle = 'Customer Details'
  contents: string;
  userTestStatus: ICustomer[] = [{
    name: 'anirudh',
    phoneNumber: '9538851205',
    email: 'ani@gmail.com',
    gender: 'm',
    state: 'ohio',
    vehicleYear: '1995',
    driverAge: '22',
    employmentStatus: 'yes',
    weeklyWage: '2000',
    maritalStatus: 'no',
    incurred1: '257349',
    incurred2: '527097',
    incurred3: '250900',
    incurred4: '110000'
},
{
  name: 'karan',
  phoneNumber: '878789989',
  email: 'karan@gmail.com',
  gender: 'm',
  state: 'washington',
  vehicleYear: '1995',
  driverAge: '22',
  employmentStatus: 'yes',
  weeklyWage: '5000',
  maritalStatus: 'no',
  incurred1: '207159',
  incurred2: '567077',
  incurred3: '250000',
  incurred4: '100000'
},
{
  name: 'manoj',
  phoneNumber: '878789989',
  email: 'manoj@gmail.com',
  gender: 'm',
  state: 'texas',
  vehicleYear: '1999',
  driverAge: '23',
  employmentStatus: 'yes',
  weeklyWage: '5005',
  maritalStatus: 'no',
  incurred1: '204159',
  incurred2: '597177',
  incurred3: '240000',
  incurred4: '150000'
},
{
  name: 'karan',
  phoneNumber: '878789989',
  email: 'kar@gmail.com',
  gender: 'm',
  state: 'california',
  vehicleYear: '2005',
  driverAge: '22',
  employmentStatus: 'yes',
  weeklyWage: '8000',
  maritalStatus: 'no',
  incurred1: '227189',
  incurred2: '561077',
  incurred3: '250300',
  incurred4: '103000'
},
{
  name: 'manoj',
  phoneNumber: '878789989',
  email: 'manoj@gmail.com',
  gender: 'm',
  state: 'arizona',
  vehicleYear: '2008',
  driverAge: '22',
  employmentStatus: 'yes',
  weeklyWage: '5000',
  maritalStatus: 'no',
  incurred1: '209959',
  incurred2: '517077',
  incurred3: '200000',
  incurred4: '90000'
},
{
  name: 'anirudh',
  phoneNumber: '878789989',
  email: 'ani@gmail.com',
  gender: 'm',
  state: 'washington',
  vehicleYear: '2009',
  driverAge: '22',
  employmentStatus: 'yes',
  weeklyWage: '9000',
  maritalStatus: 'no',
  incurred1: '222159',
  incurred2: '217077',
  incurred3: '222000',
  incurred4: '120000'
},
{
  name: 'karan',
  phoneNumber: '878789989',
  email: 'karan@gmail.com',
  gender: 'm',
  state: 'washington',
  vehicleYear: '1995',
  driverAge: '22',
  employmentStatus: 'yes',
  weeklyWage: '5000',
  maritalStatus: 'no',
  incurred1: '217759',
  incurred2: '463077',
  incurred3: '234000',
  incurred4: '983000'
}
];



  constructor(private productService: ProductService) { }
  splitted: string[];


  ngOnInit(): void{

    this.productService.getData('assets/myFile.txt')
    .subscribe(results =>
      {
        this.contents = results ;
        console.log(results)
        console.log(typeof(results))
        this.splitted = results.split('\n', 14);
        console.log(this.splitted)
        const obj: ICustomer = {
          name: this.splitted[0],
          phoneNumber: this.splitted[1],
          email: this.splitted[2],
          gender: this.splitted[3],
          state: this.splitted[4],
          vehicleYear: this.splitted[5],
          driverAge: this.splitted[6],
          employmentStatus: this.splitted[7],
          weeklyWage: this.splitted[8],
          maritalStatus: this.splitted[9],
          incurred1: this.splitted[10],
          incurred2: this.splitted[11],
          incurred3: this.splitted[12],
          incurred4: this.splitted[13]
      }
        this.userTestStatus.push(obj);
      });
  }

}
