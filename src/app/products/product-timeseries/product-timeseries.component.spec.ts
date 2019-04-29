import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductTimeseriesComponent } from './product-timeseries.component';

describe('ProductTimeseriesComponent', () => {
  let component: ProductTimeseriesComponent;
  let fixture: ComponentFixture<ProductTimeseriesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProductTimeseriesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProductTimeseriesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
