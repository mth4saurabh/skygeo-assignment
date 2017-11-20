import React, { Component } from 'react';
import config from './config';
import { Button, Col, Container, Input, InputGroup, InputGroupAddon, Row, Table } from 'reactstrap';
import './App.css';

class App extends Component {
  state = {data: [], current: '', next: '', previous: '', main: true, search: ''}

  fetchBookingItemData (url) {
    fetch(url, {
      method: 'get',
      headers: { 'Accept': 'application/json','Content-Type': 'application/json', 'Authorization': 'Basic c2t5Z2VvOnNreWdlbzIwMTc='}
    }).then((response) => response.json())
    .then((responseData) => {
      this.setState({ data: responseData.results, next: responseData.next, previous: responseData.previous, main: true });
      if (this.state.search === '') {
        this.setState({ current: url});
      }
    }).catch((error) => {
      console.log('Error');
      console.log(error);
    }); 
  };

  fetchBookingData (url) {
    fetch(url, {
      method: 'get',
      headers: { 'Accept': 'application/json','Content-Type': 'application/json', 'Authorization': 'Basic c2t5Z2VvOnNreWdlbzIwMTc='}
    }).then((response) => response.json())
    .then((responseData) => {
      this.setState({ data: responseData, main: false });
    }).catch((error) => {
      console.log('Error');
      console.log(error);
    });
  };

  updateSearch(event) {
    this.setState({ search: event.target.value });
    if (event.target.value === '') {
      this.fetchBookingItemData(this.state.current);
    } else {
      this.fetchBookingItemData(`${config.apiAddress}/booking_items/?search=`+event.target.value);
    }
  }

  format_date(booking_timestamp) {
    var t = new Date(booking_timestamp);
    var formatted = t.toISOString().substring(0, 10);
    return formatted;
  }

  content() {
    if (this.state.main) {
      return (
        <Container>
          <Row>
            <Col sm="12" md="12">
              <br />
              <InputGroup>
                <Input value={this.state.search} onChange={this.updateSearch.bind(this)} placeholder="You can search booking by id, space name, product name, venue name, booker name or email" />
                <InputGroupAddon>Go!</InputGroupAddon>
              </InputGroup>
              <br />
              <Table responsive>
                <thead>
                  <tr>
                    <th>Booking Id</th>
                    <th>Booker Name</th>
                    <th>Booker Email</th>
                    <th>Venue</th>
                    <th>Product/Space</th>
                    <th>Click for booking details</th>
                  </tr>
                </thead>
                <tbody>
                  {this.state.data.map(booking_item =>
                    <tr>
                      <th scope="row">{booking_item.booking.id}</th>
                      <td>{booking_item.booking.booker.user.first_name} {booking_item.booking.booker.user.last_name}</td>
                      <td>{booking_item.booking.booker.user.email}</td>
                      <td>{booking_item.item.venue.name}</td>
                      <td>{booking_item.item.name}</td>
                      <Button color="primary" size="md" block onClick={() => this.fetchBookingData(`${config.apiAddress}/booking_items/`+booking_item.id+`/`)}>View booking #{booking_item.booking.id}</Button>
                    </tr>
                  )}
                </tbody>
              </Table>
              <Button outline color="primary" onClick={() => this.fetchBookingItemData(this.state.previous)}>Previous</Button>{' '}
              <Button outline color="primary" onClick={() => this.fetchBookingItemData(this.state.next)}>Next</Button>{' '}
            </Col>
          </Row>
        </Container>
      );
    } else {
      return (
        <Container>
          <Row>
            <Col sm="8" md={{ size: 6, offset: 3 }}>
              <br />
              <Button color="primary" size="md" block onClick={() => this.fetchBookingItemData(this.state.current)}>Back to Main</Button>{' '}
              <br />
              <Table responsive>
                <thead>
                  <tr>
                    <th></th>
                    <th>Booking Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th>#ID</th>
                    <th>{this.state.data.booking.id}</th>
                  </tr>
                  <tr>
                    <th>Name</th>
                    <th>{this.state.data.booking.booker.user.first_name} {this.state.data.booking.booker.user.last_name}</th>
                  </tr>
                  <tr>
                    <th>Email</th>
                    <th>{this.state.data.booking.booker.user.email}</th>
                  </tr>
                  <tr>
                    <th>Prdouct/Space</th>
                    <th>{this.state.data.item.name}</th>
                  </tr>
                  <tr>
                    <th>Venue</th>
                    <th>{this.state.data.item.venue.name}</th>
                  </tr>
                  <tr>
                    <th>Total Price</th>
                    <th>{this.state.data.locked_total_price}</th>
                  </tr>
                  <tr>
                    <th>Begin Date</th>
                    <th>{this.format_date(this.state.data.start_timestamp)}</th>
                  </tr>
                  <tr>
                    <th>End Date</th>
                    <th>{this.format_date(this.state.data.end_timestamp)}</th>
                  </tr>
                </tbody>
              </Table>
            </Col>
          </Row>
        </Container>
      );
    }
  }

  componentDidMount() {
    this.fetchBookingItemData(`${config.apiAddress}/booking_items/`);
  }

  render() {
    return (
      this.content()
    );
  }
}

export default App;