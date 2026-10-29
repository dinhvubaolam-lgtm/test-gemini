## **TRƯỜNG ĐẠI HỌC CÔNG NGHỆ KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH KHOA ĐIỆN - ĐIỆN TỬ BỘ MÔN ĐIỆN CÔNG NGHIỆP** 

**ĐỒ ÁN MÔN HỌC ĐIỀU KHIỂN HỆ THỐNG ĐIỆN CÔNG NGHIỆP** 

ỨNG DỤNG THUẬT TOÁN PID ĐIỀU KHIỂN ỔN ĐỊNH MỨC NƯỚC SỬ DỤNG PLC S7-1200 

**MÃ LỚP: 261PISC414545_21 GVHD:  PGS. TS. TRẦN QUANG THỌ** 

**NHÓM 2 Mã số sinh viên Sinh viên thực hiện** Đinh Vũ Bảo Lâm 23142340 Võ Minh Thịnh 23142409 **TP. HỒ CHÍ MINH, THÁNG 11 NĂM 2026.** —— 

## **ĐẠI HỌC CÔNG NGHỆ KỸ THUẬT THÀNH PHỐ HỒ CHÍ MINH KHOA ĐIỆN - ĐIỆN TỬ BỘ MÔN ĐIỆN CÔNG NGHIỆP** 



<!-- Start of picture text -->
HCM-UTE<br><!-- End of picture text -->

# **ĐỒ ÁN MÔN HỌC** 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **LỜI CAM ĐOAN** 

i 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **LỜI CẢM ƠN** 

ii 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **MỤC LỤC** 

iii 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **DANH MỤC HÌNH** 

iv 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **DANH MỤC BẢNG** 

v 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **DANH MỤC TỪ VIẾT TẮT** 

vi 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **TÓM TẮT ĐỒ ÁN** 

vii 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **CHƯƠNG 1. TỔNG QUAN ĐỀ TÀI** 

## **1.1. Đặt vấn đề** 

- **1.2. Lý do chọn đề tài** 

- **1.3. Mục tiêu của đề tài** 

- **1.4. Đối tượng nghiên cứu** 

- **1.5. Phạm vi thực hiện** 

- **1.6. Phương pháp thực hiện** 

- **1.7. Nội dung thực hiện** 

- **1.8. Cấu trúc báo cáo** 

1 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

**CHƯƠNG 2. CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN HỆ THỐNG 2.1. Tổng quan về hệ thống điều khiển mức nước trong công nghiệp 2.2. Nguyên lý hoạt động của hệ thống ổn định mức nước 2.3. Cơ sở lý thuyết điều khiển PID 2.3.1. Cấu trúc bộ điều khiển PID liên tục và rời rạc 2.3.2. Ý nghĩa các khâu Tỷ lệ (P), Tích phân (I), Vi phân (D) 2.3.3. Các chỉ tiêu đánh giá chất lượng hệ thống điều khiển 2.3.4. Khối công nghệ PID_Compact trong PLC S7-1200** 

**2.4. Tổng quan về PLC Siemens S7-1200 2.5. Hệ thống giám sát và điều khiển HMI/SCADA trên TIA Portal V17 2.6. Biến tần và phương pháp điều khiển tốc độ động cơ bơm 3 pha 2.7. Cảm biến đo mức nước và thiết bị chấp hành 2.8. Kết luận chương 2** 

2 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

**CHƯƠNG 3. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG 3.1. Yêu cầu công nghệ và thông số kỹ thuật hệ thống 3.2. Sơ đồ khối hệ thống 3.3. Nguyên lý hoạt động chi tiết 3.4. Các chế độ hoạt động 3.5. Phân tích và phân công địa chỉ tín hiệu Input/Output (Bảng I/O) 3.6. Tính toán và lựa chọn thiết bị điện 3.6.1. Tính toán công suất và lựa chọn động cơ bơm 3 pha 3.6.2. Lựa chọn biến tần, thiết bị đóng cắt bảo vệ và cảm biến mức 3.6.3. Lựa chọn PLC S7-1200 và module mở rộng Analog** 

**3.7. Thiết kế bản vẽ sơ đồ điện 3.7.1. Thiết kế sơ đồ mạch động lực** 

**3.7.2. Thiết kế sơ đồ mạch điều khiển và kết nối PLC – Biến tần – Cảm biến 3.8. Xây dựng mô hình toán học bồn nước và thuật toán điều khiển 3.8.1. Phương trình toán học giả lập đối tượng bồn nước phục vụ mô phỏng 3.8.2. Lưu đồ thuật toán điều khiển tổng thể và điều khiển Auto PID 3.9. Thiết kế logic liên động, cảnh báo và bảo vệ 3.10. Kết luận chương 3** 

3 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

**CHƯƠNG 4. LẬP TRÌNH PLC VÀ THIẾT KẾ HỆ THỐNG SCADA/HMI 4.1. Giới thiệu phần mềm TIA Portal V17 Professional và S7-PLCSIM V17 4.2. Cấu hình phần cứng PLC S7-1200 và kết nối truyền thông ảo 4.3. Cấu trúc chương trình điều khiển trong PLC S7-1200** 

**4.4. Lập trình các chức năng điều khiển trong PLC** 

**4.4.1. Lập trình chức năng khởi động/dừng (Start/Stop) và chế độ Manual/Auto 4.4.2. Lập trình xử lý và chuẩn hóa tín hiệu Analog (NORM_X, SCALE_X) 4.4.3. Cấu hình và lập trình khối công nghệ PID_Compact trong OB30** 

**4.4.4. Lập trình khối hàm giả lập động học bồn nước (Simulated Tank Process)** 

**4.4.5. Lập trình liên động bảo vệ và xử lý cảnh báo sự cố** 

**4.5. Thiết kế giao diện điều khiển và giám sát trên SCADA/HMI** 

**4.5.1. Màn hình vận hành và giám sát chính (Main Overview Screen)** 

- **4.5.2. Màn hình cài đặt thông số PID và đồ thị đáp ứng (PID Tuning & Trend View)** 

**4.5.3. Màn hình cảnh báo và lịch sử sự cố (Alarm View)** 

**4.6. Kết luận chương 4** 

4 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

**CHƯƠNG 5. MÔ PHỎNG VÀ ĐÁNH GIÁ KẾT QUẢ TRÊN SCADA/HMI 5.1. Mục đích kiểm tra và thiết lập môi trường mô phỏng 5.2. Xây dựng kịch bản kiểm thử trên SCADA/HMI 5.3. Kết quả mô phỏng khởi động, dừng hệ thống và chế độ Manual 5.4. Kết quả mô phỏng chế độ Auto PID ổn định mức nước 5.4.1. Đáp ứng của hệ thống khi bám theo giá trị đặt ban đầu (Setpoint) 5.4.2. Đáp ứng của hệ thống khi thay đổi giá trị đặt mức nước tăng/giảm 5.4.3. Đáp ứng kháng nhiễu khi lưu lượng van xả tải tiêu thụ thay đổi đột ngột 5.4.4. Khảo sát ảnh hưởng của bộ thông số Kp, Ti, Td đến chất lượng điều khiển 5.5. Kết quả mô phỏng xử lý lỗi và cảnh báo trên SCADA/HMI 5.6. Tổng hợp và đánh giá kết quả mô phỏng 5.7. Kết luận chương 5** 

5 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

**CHƯƠNG 6. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN** 

**6.1. Kết quả đạt được 6.2. Những hạn chế của đề tài 6.3. Hướng phát triển 6.4. Kết luận chung** 

6 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **TÀI LIỆU THAM KHẢO** 

7 

SVTH: Đinh Vũ Bảo Lâm – MSSV: 23142340 SVTH: Võ Minh Thịnh – MSSV: 23142409 

## **PHỤ LỤC** 

**Phụ lục A: Chương trình điều khiển PLC S7-1200 Phụ lục B: Bảng phân công địa chỉ I/O và danh sách HMI/SCADA Tags Phụ lục C: Bản vẽ sơ đồ mạch động lực và mạch điều khiển** 

**MINH CHỨNG VIDEO BÁO CÁO ĐỒ ÁN (2 – 3 phút): [Dán link video giới thiệu và trình diễn mô phỏng tại đây]** 

1 

