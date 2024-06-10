import { Link } from 'react-router-dom';
import userPhoto from '../../../images/user-img.png'

function UserInfo() {
  return (
    <div className="user-info">
      <div className="user-photo">
        <img src={userPhoto} alt="" />
      </div>
      <div className="user-description">
        <p>Фамилия Имя Отчество</p>
        <p className="user-id">ID_001</p>
        <Link to="/profile-edit" className='edit-profile-link'>Редактировать профиль</Link>
      </div>
    </div>
  );
}

export default UserInfo;
