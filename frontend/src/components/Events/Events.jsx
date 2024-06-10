import Event1 from "../../images/Events/event1.jpg";
import Event2 from "../../images/Events/event2.jpg";
import Event3 from "../../images/Events/event3.jpg";
import Event5 from "../../images/Events/event5.jpg";
import Event4 from "../../images/Events/event4.jpg";
import Event6 from "../../images/Events/event6.jpg";
import Event7 from "../../images/Events/event7.jpg";
import Event8 from "../../images/Events/event8.png";

import { Link } from "react-router-dom";

function Events() {
  return (
    <>
      <div className="events-container">
        <Link to="/main">
          <i className="fas fa-home"></i>
        </Link>
        <div className="events-content">
          <div className="events-title">
            <p>Последние события нашего университета</p>
          </div>
          <div className="events-items">
            <div className="events-item">
              <img src={Event1} alt="event image" />
            </div>
            <div className="events-item">
              <img src={Event2} alt="event image" />
            </div>
            <div className="events-item">
              <img src={Event4} alt="event image" />
            </div>
            <div className="events-item">
              <img src={Event3} alt="event image" />
            </div>
            <div className="events-item">
              <img src={Event6} alt="event image" />
            </div>
            <div className="events-item">
              <img src={Event7} alt="event image" />
            </div>
            <div className="events-item">
              <img src={Event5} alt="event image" />
            </div>
            <div className="events-item">
              <img src={Event8} alt="event image" />
            </div>
          </div>
        </div>
      </div>
      <footer>
        <div>
          <Link to="">Подать<br/>документы</Link>
        </div>
        <div>
          <p>Контакты:</p>
          <p>+7 xxx xxx-xx-xx</p>
        </div>
        <div>
          <ul>
            <li>
              <Link to="#">VK</Link>
            </li>
            <li>
              <Link to="#">Telegram</Link>
            </li>
            <li>
              <Link to="#">Instagram</Link>
            </li>
          </ul>
        </div>
      </footer>
    </>
  );
}

export default Events;
