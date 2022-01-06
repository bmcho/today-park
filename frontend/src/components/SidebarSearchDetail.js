import React, { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { Header } from "./Header";
import Map from "./Map";
import ReactTooltip from "react-tooltip";
import { ReactComponent as BackIcon } from "../image/back.svg";
import { ReactComponent as BookmarkIcon } from "../image/bookmark-maked.svg";
import { SidebarMenu } from "./SidebarMenu";
import { getParkDetail, getReviews } from "../actions/index";
import { DetailList } from "./DetailList";
import { SimpleMap } from "./GoolgleMap";
import { Review } from "./Review";

export function SidebarSearchDetail() {
  const [content, setContent] = useState("");
  const [detailData, setDetailData] = useState("");
  const [detailList, setDetailList] = useState("");
  const [equitments, setEquitments] = useState([]);
  const [simplemap, setSimplemap] = useState("");
  const [reviewList, setreviewList] = useState("");

  const { id } = useParams();

  // 마운트시, 공원 상세 정보 GET 요청, 리뷰 정보 GET요청
  useEffect(() => {
    async function getParkdetail() {
      const response = await getParkDetail(id);
      try {
        setDetailData(response);
        setEquitments(response.equipments);
        console.log(response);
      } catch (error) {
        console.log("공원 정보 get요청 실패");
      }
    }
    async function getreviews() {
      const response = await getReviews(id);
      try {
        setreviewList(response);
      } catch (error) {
        console.log("리뷰 정보 get 요청 실패");
      }
    }
    getParkdetail();
    getreviews();
  }, []);

  // GET 요청 후, 상세 페이지, 구글맵 UI
  useEffect(() => {
    setDetailList(
      <DetailList detailData={detailData} equitments={equitments} />
    );
    detailData &&
      setSimplemap(
        <SimpleMap
          center={{
            lat: Number(detailData.latitude),
            lng: Number(detailData.longitude),
          }}
          zoom={15}
        />
      );
  }, [detailData, equitments]);

  return (
    <>
      <Header />
      <section className="search">
        <SidebarMenu item={"search"} />
        <div className="sidebar">
          <Link to="/search">
            <BackIcon width="24" height="24" className="backIcon" />
          </Link>
          <div className="mapAPI">{detailData && simplemap}</div>
          <div className="parkDetailContainer">
            <div className="parkDetail">{detailData && detailList}</div>

            <form className="createReview">
              <textarea placeholder="내용을 입력해주세요." />
              <br />
              <button type="submit">등록하기</button>
            </form>
            <div className="reviews">
              {reviewList &&
                reviewList.map((item, idx) => {
                  return <Review key={idx} item={item} idx={idx} />;
                })}
            </div>
          </div>
        </div>
        <Map setTooltipContent={setContent} />
        <ReactTooltip>{content}</ReactTooltip>
      </section>
    </>
  );
}
