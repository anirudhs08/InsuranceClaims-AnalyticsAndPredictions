import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TimeseriesGraphComponent } from './timeseries-graph.component';

describe('TimeseriesGraphComponent', () => {
  let component: TimeseriesGraphComponent;
  let fixture: ComponentFixture<TimeseriesGraphComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TimeseriesGraphComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TimeseriesGraphComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
