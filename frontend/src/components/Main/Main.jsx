import { Link } from "react-router-dom";

import AdmissioinsOffice from "./AdmissionsOffice/AdmissionsOffice";
import Structure from "./Structure/Structure";
import Questions from "./Questions/Questions";

import headerImg from "../../images/main-header-img.png";
import userImg from "../../images/user-img.png";

function Main() {
  return (
    <>
      <header>
        <Link to="/login" className="header-profile">
          <img src={userImg} alt="user img" />
        </Link>
        <img
          className="header-background-img"
          src={headerImg}
          alt="header img"
        />
      </header>
      <AdmissioinsOffice />
      <Structure />
      <Questions />
      <footer>
        <p>Перейдите в раздел <Link to="/events">новости</Link>, что бы узнать нас лучше </p>
      </footer>
    </>
  );
}

export default Main;
