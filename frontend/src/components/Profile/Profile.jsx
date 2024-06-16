import { Link } from "react-router-dom";

import UserInfo from "./UserInfo/UserInfo";
import AdmissionDate from "./AdmissionDate/AdmissionDate";
import ProfileForm from "./ProfileForm/ProfileForm";

function Profile() {
  return (
    <div className="profile-container">
      <div className="profile-menu">
        <Link to="/main">
          <i className="fas fa-home"></i>
        </Link>
      </div>
      <div className="profile-content">
        <UserInfo />
        <AdmissionDate />
      </div>
      <ProfileForm />
    </div>
  );
}

export default Profile;
