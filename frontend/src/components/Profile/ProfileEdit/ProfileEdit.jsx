import { Link } from "react-router-dom";

import userPhoto from "../../../images/user-img.png";

function ProfileEdit() {
  return (
    <div className="profile-edit-container">
      <p className="profile-edit-title">Внесите изменения</p>
      <div className="profile-edit-content">
        <div className="profile-edit-user-photo">
          <img src={userPhoto} alt="user photo" />
        </div>
        <form className="profile-edit-form">
          <div>
            <input type="text" id="profile-edit-form-surname" />
            <label htmlFor="profile-edit-form-surname">Фамилия</label>
          </div>
          <div>
            <input type="text" id="profile-edit-form-name" />
            <label htmlFor="profile-edit-form-name">Имя</label>
          </div>
          <div>
            <input type="text" id="profile-edit-form-patronymic" />
            <label htmlFor="profile-edit-form-patronymic">Отчество</label>
          </div>
          <div>
            <input type="tel" id="profile-edit-form-phone" />
            <label htmlFor="profile-edit-form-phone">Телефон</label>
          </div>
          <div>
            <input type="email" id="profile-edit-form-email" />
            <label htmlFor="profile-edit-form-email">Почта</label>
          </div>
        </form>
      </div>
      <div className="buttons">
        <Link to="/profile" className="profile-edit-form-cancel">
          <i class="fas fa-times"></i>
        </Link>
        <button className="profile-edit-form-submit">
          <i class="fas fa-check"></i>
        </button>
      </div>
    </div>
  );
}

export default ProfileEdit;
